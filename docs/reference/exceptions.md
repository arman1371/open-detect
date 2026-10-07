# Errors

Every exception raised deliberately by the library derives from `UniDetectError`.

::: unidetect.exceptions
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false

::: unidetect.algorithms.auto_validate.exceptions
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false

`UnknownAlgorithmError` (from `unidetect.algorithms`) is raised by `get_algorithm` for an
unregistered name.
