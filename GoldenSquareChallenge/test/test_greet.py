from lib.greet import *

def test_greet_returns_hello_name():
    # We run the function with an example argument 3.
    result = greet("Joan")

    # And then assert that in this example it should return 8.
    assert result == "Hello, Joan!"