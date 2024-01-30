import pytest
from src.lambdas.parser.parsing.volume_targets_parser import VolumeTargetsParser
from tests.lambdas.parser.parsing.fixtures.expected_parsed_agent_volume_targets import expected_parsed_volume_targets_result


@pytest.fixture
def volume_sales_targets_file_content():
    with open("./tests/lambdas/parser/parsing/fixtures/agent_volume_sales_targets_1989.xlsx", "rb") as file:
        return file.read()


def test_parse_matrices(volume_sales_targets_file_content, expected_parsed_volume_targets_result):
    # Arrange.
    parser = VolumeTargetsParser()
    year = "1989"
    expected_result = expected_parsed_volume_targets_result

    # Act
    result = parser.parse_volume_targets(volume_sales_targets_file_content)

    # Assert
    assert result == expected_result