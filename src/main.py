import html
import importlib
import inspect
import json
import re
from pathlib import Path
from re import Match
from textwrap import dedent
from typing import Any, ClassVar, Dict

import mistune
from mistune import BlockParser, BlockState, InlineParser, InlineState, Markdown
from mistune.directives import Admonition, FencedDirective, TableOfContents
from mistune.directives._base import DirectivePlugin
from mistune.renderers.markdown import MarkdownRenderer

OUTPUT = "graph_docs_output"


def remove_jinja(md: Markdown):
    JINJA_PATTERN = r"\{\{ \w+ \}\}"

    def parse_inline_jinja(inline: InlineParser, m: Match, state: InlineState):
        return m.end()

    md.inline.register("inline_jinja", JINJA_PATTERN, parse_inline_jinja, before="link")


def clean_generic_inline_directives(md: Markdown):
    INLINE_DIRECTIVE_PATTERN = (
        r"\{[A-Za-z\.:\-]+\}`(?P<directive_name>[A-Z_a-z\.\s\(\)]*)`"
    )

    def parse_inline_directive(inline: InlineParser, m: Match, state: InlineState):
        name = m.group("directive_name")
        state.append_token({"type": "text", "raw": name})
        return m.end()

    md.inline.register(
        "inline_directive",
        INLINE_DIRECTIVE_PATTERN,
        parse_inline_directive,
        before="link",
    )


def clean_inline_api_references(md: Markdown):
    API_REF_PATTERN = r"\{[A-Za-z.:\-]+\}`(?P<truncated>~)?(?P<api_name>[A-Z_a-z\.]+)\s*(\<[A-Za-z.]+\>)?(\(\))?`"  # noqa

    def parse_inline_api_rference(inline: InlineParser, m: Match, state: InlineState):
        name = m.group("api_name")
        if m.group("truncated"):
            name = name.split(".").pop()
        state.append_token({"type": "codespan", "raw": name})
        return m.end()

    md.inline.register(
        "inline_api_ref",
        API_REF_PATTERN,
        parse_inline_api_rference,
        before="inline_directive",
    )


class CodeBlock(DirectivePlugin):
    SUPPORTED_NAMES = {"code-block"}

    def parse(self, block: BlockParser, m: Match, state: BlockState):
        language = self.parse_title(m)
        options = dict(self.parse_options(m))
        content = self.parse_content(m)

        if caption := options.get("caption"):
            content = f"# {caption}\n" + content

        return {
            "type": "block_code",
            "raw": content.strip(),
            "style": "fenced",
            "marker": "```",
            "attrs": {"info": language + " copy"},
        }

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)


class CodeInclude(DirectivePlugin):
    SUPPORTED_NAMES = {"code-include"}

    def parse(self, block: BlockParser, m: Match, state: BlockState):
        options = dict(self.parse_options(m))
        if (func := options.get("func")) or (func := options.get("class")):
            func_path = func[1:-1].split(".")
            if func_path[-2][0].isupper():
                class_, func = func_path[-2:]
                import_path = ".".join(func_path[:-2])
                module = importlib.import_module(import_path)
                func_obj = getattr(getattr(module, class_), func)
            else:
                func = func_path[-1]
                import_path = ".".join(func_path[:-1])
                module = importlib.import_module(import_path)
                func_obj = getattr(module, func)

            source = inspect.getsource(func_obj)

            return {
                "type": "block_code",
                "raw": dedent(source).strip(),
                "style": "fenced",
                "marker": "```",
                "attrs": {"info": "python" + " copy"},
            }

        return {"type": "blank_line"}

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)


class TabSet(DirectivePlugin):
    SUPPORTED_NAMES = {"tab-set"}

    def parse(self, block: BlockParser, m: Match, state: BlockState):
        content = self.parse_content(m)

        new_state = block.state_cls()
        new_state.process(dedent(content))
        block.parse(new_state)

        items: list[str] = []
        for token in new_state.tokens:
            if token and token["type"] == "tab_item" and (name := token["name"]):
                items.append(name)

        return {
            "type": "tab_set",
            "style": "fenced",
            "items": items,
            "children": new_state.tokens,
        }

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)


class TabItem(DirectivePlugin):
    SUPPORTED_NAMES = {"tab-item"}

    def parse(self, block: BlockParser, m: Match, state: BlockState):
        content = self.parse_content(m)
        title = self.parse_title(m)

        new_state = block.state_cls()
        new_state.process(dedent(content))
        block.parse(new_state)

        return {
            "type": "tab_item",
            "name": title,
            "style": "fenced",
            "children": new_state.tokens,
        }

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)


class Grid(DirectivePlugin):
    SUPPORTED_NAMES = {"grid"}

    def parse(self, block: BlockParser, m: Match, state: BlockState):
        content = self.parse_content(m)

        new_state = block.state_cls()
        new_state.process(dedent(content))
        block.parse(new_state)

        return {
            "type": "list",
            "children": [
                {
                    "type": "list_item",
                    "children": [
                        token,
                        {"type": "blank_line"},
                        {
                            "type": "list",
                            "children": [
                                {
                                    "type": "list_item",
                                    "children": [
                                        {"type": "text", "raw": token["attrs"]["body"]}
                                    ],
                                }
                            ],
                            "tight": False,
                            "bullet": "\n*",
                            "attrs": {
                                "depth": 1,
                                "ordered": False,
                            },
                        },
                    ],
                }
                for token in new_state.tokens
                if token.get("type") == "link"
            ],
            "tight": True,
            "bullet": "*",
            "attrs": {
                "depth": 0,
                "ordered": False,
            },
        }

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)


class GridItemCard(DirectivePlugin):
    SUPPORTED_NAMES = {"grid-item-card"}
    CURRENT_FILE: ClassVar[Path]

    def parse(self, block: BlockParser, m: Match, state: BlockState):
        content = self.parse_content(m)
        options = dict(self.parse_options(m))

        new_state = block.state_cls()
        new_state.process(dedent(content))
        block.parse(new_state)

        if len(new_state.tokens) == 7:
            # yea, it's just how the cards are laid out
            _, _, header, _, _, _, body = new_state.tokens
            header = (
                header["text"]
                .replace("{bdg-light}`INVIS`", "")
                .replace("{{ lab_bdg }}", "")
                .strip()
            )
            body = body["text"].strip()

        elif len(new_state.tokens) == 3:
            header, _, body = new_state.tokens
            header = header["raw"].split("\n")[1].strip()
            body = body["text"].strip()

        else:
            raise Exception("Unhandled Grid Item Card Type")

        prefix_path = "/".join(self.CURRENT_FILE.parent.parts[2:])
        link = options["link"].replace("/index", "/")

        if not link.startswith(".."):
            link = f"{prefix_path}/{link}"
        elif "index" in str(self.CURRENT_FILE):
            link = link.replace("../", "")

        return {
            "type": "link",
            "children": [{"type": "text", "raw": header}],
            "attrs": {"url": link, "body": body},
        }

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)


class MDXRenderer(MarkdownRenderer):
    NAME: str = "mdx"
    CURRENT_FILE: ClassVar[Path]

    def inline_html(self, token: dict[str, Any], state: BlockState):
        if "only-dark" in token["raw"]:
            return ""
        return super().inline_html(token, state)

    def codespan(self, token: dict[str, Any], state: BlockState):
        token["raw"] = html.unescape(token["raw"])
        return super().codespan(token, state)

    def heading(self, token: Dict[str, Any], state: BlockState) -> str:
        if token["attrs"].get("level", 0) == 1:
            title = token["children"][0]["raw"]
            return f"---\ntitle: {title}\n---\n\n"
        return super().heading(token, state)

    def tab_set(self, token: dict[str, Any], state: BlockState):
        inner = self.render_children(token, state)
        items = ", ".join(f"'{item}'" for item in token["items"])

        return f"<Tabs items={{[{items}]}}>\n{inner}</Tabs>\n"

    def tab_item(self, token: dict[str, Any], state: BlockState):
        inner = self.render_children(token, state)

        return f"<Tabs.Tab>\n{inner.strip()}\n</Tabs.Tab>\n"

    def admonition(self, token: dict[str, Any], state: BlockState):
        inner = self.render_children(token, state)

        match token.get("attrs", {}).get("name", "info"):
            case "important" if "interactive" in inner:
                return "\n"
            case "warning" if "Run Code" in inner:
                return "\n"
            case "note":
                callout = "info"
            case "error" | "warning" as name:
                callout = name
            case _:
                callout = "default"

        return f'<Callout type="{callout}">\n{inner}</Callout>\n\n'

    def admonition_title(self, token: dict[str, Any], state: BlockState):
        return ""

    def admonition_content(self, token: dict[str, Any], state: BlockState):
        if "children" in token:
            return self.render_children(token, state)
        return self.text(token, state)

    def block_html(self, token: dict[str, Any], state: BlockState):
        if "<!--" in token.get("raw", ""):
            return ""
        elif "only-dark" in token["raw"]:
            return ""
        elif "figure" in token["raw"]:
            return ""
        token["raw"] = re.sub(r'\sstyle=".+?"', "", token["raw"])
        return super().block_html(token, state)

    def def_list(self, token: dict[str, Any], state: BlockState):
        inner = self.render_children(token, state)
        return "<dl style={{margin:'revert'}}>\n" + inner + "</dl>\n\n"

    def def_list_head(self, token: dict[str, Any], state: BlockState):
        inner = self.render_children(token, state)
        return "\t<dt style={{margin:'revert'}}>\n\t" + inner + "\n\t</dt>\n"

    def def_list_item(self, token: dict[str, Any], state: BlockState):
        inner = self.render_children(token, state)
        return "\t<dd style={{margin:'revert'}}>\n\t" + inner + "\t</dd>\n"

    def link(self, token: dict[str, Any], state: BlockState):
        if "index" in token["attrs"]["url"]:
            token["attrs"]["url"] = token["attrs"]["url"].replace("index.md", "")
        if self.CURRENT_FILE.stem == "index":
            prefix_path = "/".join(self.CURRENT_FILE.parent.parts[3:])
            token["attrs"]["url"] = prefix_path + "/" + token["attrs"]["url"]
        return super().link(token, state)


markdown = mistune.create_markdown(
    escape=False,
    renderer=MDXRenderer(),
    plugins=[
        "def_list",
        remove_jinja,
        clean_inline_api_references,
        clean_generic_inline_directives,
        FencedDirective(
            [
                CodeInclude(),
                Grid(),
                GridItemCard(),
                TabSet(),
                TabItem(),
                CodeBlock(),
                Admonition(),
                TableOfContents(),
            ],
            ":",
        ),
        FencedDirective(
            [
                CodeInclude(),
                Grid(),
                GridItemCard(),
                TabSet(),
                TabItem(),
                CodeBlock(),
                Admonition(),
                TableOfContents(),
            ]
        ),
    ],
)

data = json.loads(Path("src/paths.json").read_text())
output = Path(OUTPUT)

raw_paths = (Path(file) for file in data.get("files", []))

paths: list[Path] = []
for path in raw_paths:
    if path.is_dir():
        paths.extend(path.glob("**/*.md"))
    else:
        paths.append(path)

for path in paths:
    file_path = output / str(path).replace("docs/", "")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.stem == "index":
        file_path = file_path.parent

    GridItemCard.CURRENT_FILE = path
    MDXRenderer.CURRENT_FILE = path

    if path.with_suffix(".mdx").exists():
        text = path.with_suffix(".mdx").read_text()
    else:
        try:
            text = markdown(path.read_text())
        except Exception as err:
            print("Exception in", path)
            raise err

        if "Callout" in text:
            text = "import { Callout } from 'nextra/components'\n\n" + text
        if "Tabs" in text:
            text = "import { Tabs } from 'nextra/components'\n\n" + text

    file_path.with_suffix(".mdx").write_text(text)
