import enum

from .enums import BuildLibraries, ExportLibraries


class Settings(enum.Enum):
    BUILD_LIBRARY_SERVICE = BuildLibraries.FITZ.value
    EXPORT_LIBRARY_SERVICE = ExportLibraries.FITZ.value
