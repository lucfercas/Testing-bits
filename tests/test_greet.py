from lib.greet import *

def test_greet_returns_given_name():
    result = greet('Alice')
    assert result == 'Hello, Alice!'