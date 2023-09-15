# Adjusting Subgrounds Logging

Subgrounds uses the default python logger frequently with varying levels. While we leverage warnings to help let end-users catch mistakes earlier, we also use the info level to help debug and find errors.

In normal usage of subgrounds, you may never see any of these debug messages apart from some rare warnings if you are using deprecated APIs. However, if you are using subgrounds in a project and want to use the python logger, you might find it useful to ignore the info log levels via this recipe:

```{code-block} python
:caption: Ignores any logs lower than warning from the `subgrounds` library

import logging
logging.getLogger("subgrounds").setLevel(logging.WARNING)
```

You are free to use any level of logging for your own project while ignoring lower level logs from `subgrounds`.
