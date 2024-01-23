from enum import Enum


class FileTypeUnknownError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class FileType(Enum):
    MATRICES = 1
    VOLUME_TARGETS = 2


class FileMetadata:
    def __init__(self, file_name):
        self.file_name = file_name
        self.year = self._extract_year_from_file_name(file_name)
        self.file_type = self._get_file_type(file_name)

    def _get_file_type(self, file_name: str) -> FileType:
        if file_name.startswith("commission_matrices"):
            return FileType.MATRICES
        elif file_name.startswith("agent_volume_sales_targets"):
            return FileType.VOLUME_TARGETS
        else:
            raise FileTypeUnknownError(f"Could not derive a file type from the provided file name: {file_name}.")
    
    def _extract_year_from_file_name(self, file_name: str) -> str:
        year = file_name.split("_")[-1].split(".")[0]
        return year