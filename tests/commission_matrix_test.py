import pytest
from src.common.commission_matrix import CommissionMatrix, CommissionResult

# Sample JSON structure for testing
sample_json = {
    'matrix': [[0.15, 0.17, 0.19], 
               [0.10, 0.12, 0.14],
               [0.05, 0.07, 0.09]],
    'x-axis': [0.5, 0.6, 0.7],
    'y-axis': [0.6, 0.7, 0.8]
}

# Test initialization and basic eligibility
def test_initialization():
    cm = CommissionMatrix(sample_json)
    assert cm.matrix == [[0.15, 0.17, 0.19], 
                         [0.10, 0.12, 0.14],
                         [0.05, 0.07, 0.09]]
    assert cm.x_axis == [0.5, 0.6, 0.7]
    assert cm.y_axis == [0.6, 0.7, 0.8]

def test_eligibility_not_eligible():
    cm = CommissionMatrix(sample_json)
    result = cm.get_commission(0.04, 0.10)
    assert not result.eligible and result.commission == 0

def test_commission_calculation():
    cm = CommissionMatrix(sample_json)
    result = cm.get_commission(0.9, 0.9)
    assert result.eligible and result.commission == 0.07

