from PDFFiller.constants.settings import Settings
from PDFFiller.constants.enums import ExportLibraries

from .fitz_export_service import FitzExportService


class ExportServiceFactory:

    @staticmethod
    def build_object(service=Settings.EXPORT_LIBRARY_SERVICE.value):
        if service == ExportLibraries.FITZ.value:
            return FitzExportService()

        raise NotImplementedError()
