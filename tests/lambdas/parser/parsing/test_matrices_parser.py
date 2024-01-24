import pytest
from src.lambdas.parser.parsing.matrices_parser import CommissionMatricesParser
from tests.lambdas.parser.parsing.fixtures.expected_parsed_matrices import expected_parsed_matrices_result


@pytest.fixture
def commission_matrices_file_content():
    with open("./tests/lambdas/parser/parsing/fixtures/commission_matrices_1989.xlsx", "rb") as file:
        return file.read()


def test_parse_matrices(commission_matrices_file_content, expected_parsed_matrices_result):
    # Arrange.
    parser = CommissionMatricesParser()
    year = "1989"
    expected_result = expected_parsed_matrices_result

    # Act
    result = parser.parse_matrices(commission_matrices_file_content, year)

    # Assert
    assert result == expected_result