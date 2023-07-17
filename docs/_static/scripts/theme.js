function setTheme(mode) {
    if (mode !== "light" && mode !== "dark" && mode !== "auto") {
        console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
        mode = "auto";
    }

    document.body.dataset.theme = mode;
    localStorage.setItem("theme", mode);
    console.log(`Changed to ${mode} mode.`);
}

////////////////////////////////////////////////////////////////////////////////
// Main entrypoint
////////////////////////////////////////////////////////////////////////////////
function main() {
    const prefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;
    const currentTheme = localStorage.getItem("theme") || "unset";

    if (!prefersLight && currentTheme === "unset") {
        setTheme("dark");
    }
}

document.addEventListener("DOMContentLoaded", main);
