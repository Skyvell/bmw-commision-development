import pytest
from decimal import Decimal


@pytest.fixture
def expected_parsed_matrices_result():
    data = [
        {
            'market': 'Sweden',
            'year': '1989',
            'matrix': {
                'x_axis': [Decimal('0.7'), Decimal('0.85'), Decimal('1.0'), Decimal('1.15')],
                'y_axis': [Decimal('0.3'), Decimal('0.4'), Decimal('0.5'), Decimal('0.6'), Decimal('0.65'), Decimal('0.7'), Decimal('0.75'), Decimal('0.8'), Decimal('0.85'), Decimal('0.9'), 1],
                'values': [
                    [Decimal('0.0222'), Decimal('0.0235'), Decimal('0.026'), Decimal('0.027')],
                    [Decimal('0.022'), Decimal('0.023'), Decimal('0.025'), Decimal('0.026')],
                    [Decimal('0.0212'), Decimal('0.0225'), Decimal('0.0235'), Decimal('0.0245')],
                    [Decimal('0.021'), Decimal('0.022'), Decimal('0.024'), Decimal('0.025')],
                    [Decimal('0.0202'), Decimal('0.0215'), Decimal('0.0225'), Decimal('0.0235')],
                    [Decimal('0.02'), Decimal('0.021'), Decimal('0.023'), Decimal('0.024')],
                    [Decimal('0.0192'), Decimal('0.0205'), Decimal('0.0215'), Decimal('0.0225')],
                    [Decimal('0.019'), Decimal('0.02'), Decimal('0.022'), Decimal('0.023')],
                    [Decimal('0.018'), Decimal('0.019'), Decimal('0.021'), Decimal('0.022')],
                    [Decimal('0.017'), Decimal('0.018'), Decimal('0.02'), Decimal('0.021')],
                    [Decimal('0.016'), Decimal('0.017'), Decimal('0.019'), Decimal('0.02')]
                ]
            }
        },
        {
            'market': 'Finland',
            'year': '1989',
            'matrix': {
                'x_axis': [Decimal('0.7'), Decimal('0.9'), Decimal('1.0'), Decimal('1.15')],
                'y_axis': [Decimal('0.3'), Decimal('0.4'), Decimal('0.5'), Decimal('0.6'), Decimal('0.65'), Decimal('0.7'), Decimal('0.75'), Decimal('0.8'), Decimal('0.85'), Decimal('0.9'), 1],
                'values': [
                    [Decimal('0.0222'), Decimal('0.0235'), Decimal('0.026'), Decimal('0.027')],
                    [Decimal('0.022'), Decimal('0.023'), Decimal('0.025'), Decimal('0.026')],
                    [Decimal('0.0212'), Decimal('0.0225'), Decimal('0.0235'), Decimal('0.0245')],
                    [Decimal('0.021'), Decimal('0.022'), Decimal('0.024'), Decimal('0.025')],
                    [Decimal('0.0202'), Decimal('0.0215'), Decimal('0.0225'), Decimal('0.0235')],
                    [Decimal('0.02'), Decimal('0.021'), Decimal('0.023'), Decimal('0.024')],
                    [Decimal('0.0192'), Decimal('0.0205'), Decimal('0.0215'), Decimal('0.0225')],
                    [Decimal('0.019'), Decimal('0.02'), Decimal('0.022'), Decimal('0.023')],
                    [Decimal('0.018'), Decimal('0.019'), Decimal('0.021'), Decimal('0.022')],
                    [Decimal('0.017'), Decimal('0.018'), Decimal('0.02'), Decimal('0.021')],
                    [Decimal('0.0165'), Decimal('0.017'), Decimal('0.019'), Decimal('0.02')]
                ]
            }
        }
    ]
    return data
