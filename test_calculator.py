from apps.python_modules import add,subtract,generate_random_number


def test_addition():
    assert add(2,3) == 5
    ''' In Python, assert means “check that this condition is true.”
    it means:
    call the add function with 2 and 3
    check whether the result is equal to 5
    if it is, nothing happens
    if it is not, Python raises an AssertionError
'''

def test_subtract():
    assert subtract(3,2) == 1