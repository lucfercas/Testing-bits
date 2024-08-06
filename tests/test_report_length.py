from lib.report_length import *

def test_returns_correct_length():
    result = report_length('house')
    assert result == 'This string was 5 characters long.'
