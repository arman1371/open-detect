# Errors

Every exception raised deliberately by the library derives from `OpenDetectError`.

::: open_detect.exceptions
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false

::: open_detect.algorithms.auto_validate.exceptions
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false

`UnknownAlgorithmError` (from `open_detect.algorithms`) is raised by `get_algorithm` for an
unregistered name.
