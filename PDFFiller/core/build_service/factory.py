from PDFFiller.constants.settings import Settings
from PDFFiller.constants.enums import BuildLibraries

from .fitz_build_service import FitzBuildService


class BuildServiceFactory:

    @staticmethod
    def build_object(debug, service=Settings.BUILD_LIBRARY_SERVICE.value):
        print(service, BuildLibraries.FITZ.value)
        if service == BuildLibraries.FITZ.value:
            return FitzBuildService(debug)

        raise NotImplementedError()
