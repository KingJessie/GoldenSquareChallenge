from lib.report_length import *

def test_return_length_of_string():
    result = report_length("testing")
    assert result ==  "This string was 7 characters long."