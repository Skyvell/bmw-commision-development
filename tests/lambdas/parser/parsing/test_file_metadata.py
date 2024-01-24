import pytest
from src.lambdas.parser.parsing.file_metadata import FileMetadata, FileType, FileTypeUnknownError


def test_file_metadata_with_matrices_file():
    # Arrange.
    file_name = "commission_matrices_2020.xlsx"

    # Act.
    file_metadata = FileMetadata(file_name)

    # Assert.
    assert file_metadata.year == "2020"
    assert file_metadata.file_type == FileType.MATRICES

def test_file_metadata_with_volume_targets_file():
    # Arrange.
    file_name = "agent_volume_sales_targets_2020.xlsx"

    # Act.
    file_metadata = FileMetadata(file_name)

    # Assert.
    assert file_metadata.year == "2020"
    assert file_metadata.file_type == FileType.VOLUME_TARGETS

def test_file_metadata_with_unknown_file():
    # Arrange.
    file_name = "unknown_file_type_2020.xlsx"

    # Act & Assert.
    with pytest.raises(FileTypeUnknownError):
        FileMetadata(file_name)