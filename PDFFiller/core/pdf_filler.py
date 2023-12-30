from PDFFiller.exceptions import UnableToBuild, NothingToExport, UnableToExport

from .build_service import BuildServiceFactory
from .export_service import ExportServiceFactory


class PDFFiller:

    def __init__(self, debug=False):
        self.pdf_streams = []
        self.debug = debug
        self.build_service = BuildServiceFactory.build_object(self.debug)
        self.export_service = ExportServiceFactory.build_object()

    def build(self, template):
        try:
            pdf_stream = self.build_service.build(template)
            self.pdf_streams.append(pdf_stream)
        except Exception as exception:
            raise UnableToBuild(exception=exception)
        return self

    def reset(self):
        self.pdf_streams = []
        return self

    def export(self, destination=""):
        if len(self.pdf_streams) == 0:
            raise NothingToExport()
        try:
            self.export_service.export_file_system(self.pdf_streams, destination)
        except Exception as exception:
            raise UnableToExport(exception=exception)
        return self

    def done(self):
        if len(self.pdf_streams) == 0:
            raise None

        raw_data = self.export_service.export_raw(self.pdf_streams)
        self.pdf_streams = []
        return raw_data

