class ProjectException(Exception):
    def __init__(self, exception=None, **kwargs):
        self.exception = exception
        self.additional_info = kwargs
        super().__init__(self.exception)


class UnableToBuild(ProjectException):
    code = "UNABLE_TO_BUILD"


class NothingToExport(ProjectException):
    code = "NOTHING_TO_EXPORT"


class UnableToExport(ProjectException):
    code = "UNABLE_TO_EXPORT"
