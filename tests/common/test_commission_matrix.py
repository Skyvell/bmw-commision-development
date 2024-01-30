import pytest
from src.common.commission_matrix import CommissionMatrix


# Arrange.
commission_matrix = {
    'values': [[0.15, 0.17, 0.19], 
               [0.10, 0.12, 0.14],
               [0.05, 0.07, 0.09]],
    'x-axis': [0.5, 0.6, 0.7],
    'y-axis': [0.6, 0.7, 0.8]
}


def test_initialization():
    # Arrange.
    cm = CommissionMatrix(commission_matrix, "2017", "Sweden")

    # Assert.
    assert cm.values == [[0.15, 0.17, 0.19], 
                         [0.10, 0.12, 0.14],
                         [0.05, 0.07, 0.09]]
    assert cm.x_axis == [0.5, 0.6, 0.7]
    assert cm.y_axis == [0.6, 0.7, 0.8]


def test_commission_calculations():
    # Arrange.
    test_cases = [
        # These tests should all yield no commission.
        {"x": 0.04999, "y": 0.8, "expected_commission": 0, "expected_eligible": False},
        {"x": 0.7, "y": 0.5999, "expected_commission": 0, "expected_eligible": False},
        {"x": 0.4999, "y": 0.5999, "expected_commission": 0, "expected_eligible": False},

        # These tests should all yield a commission with different values.
        {"x": 0.9, "y": 0.9, "expected_commission": 0.19, "expected_eligible": True},
        {"x": 0.6, "y": 0.7, "expected_commission": 0.12, "expected_eligible": True},
        {"x": 0.5, "y": 0.6, "expected_commission": 0.05, "expected_eligible": True},
        {"x": 0.7, "y": 0.8, "expected_commission": 0.19, "expected_eligible": True},
        {"x": 0.55, "y": 0.65, "expected_commission": 0.05, "expected_eligible": True}
    ]
    cm = CommissionMatrix(commission_matrix, "2017", "Sweden")

    # Act and assert.
    for case in test_cases:
        result = cm.get_commission(case["x"], case["y"])
        assert result.eligible == case["expected_eligible"] and result.commission == case["expected_commission"]

    

