import sys

if sys.version_info < (3, 7):
    from ._mode import ModeValidator
    from ._minsize import MinsizeValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._mode.ModeValidator", "._minsize.MinsizeValidator"]
    )
