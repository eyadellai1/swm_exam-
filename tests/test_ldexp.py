# tests/test_ldexp.py
import math
import pytest




def wrapper(x,i):
    if not x or not i:
        raise ValueError("provide integers, currently x or i is missing ")
    print(isinstance(x,int))
    if isinstance(x,int) and isinstance(i,int):
        return math.ldexp(x,i)
    else:
        raise ValueError("provide integers, currently x or i is not integers")

class TestMathLdexp:
    def test_positive_numbers(self):
        # Verify that tracked_ldexp behaves like math.ldexp
        print(wrapper(9,3))
        assert wrapper(9, 3) == 72

    def test_negative_numbers(self):
        # Verify with negative numbers
        assert wrapper(-5, 2) == math.ldexp(-5, 2)

    def test_fractional_x(self):
        # Verify fractional numbers
       with pytest.raises(ValueError):
        assert wrapper(0.5, 2)

    def test_string(self):
        # Verify with x = 0
       with pytest.raises(ValueError):
        assert wrapper("eya", 5)

    def test_missing(self):
        # Verify with a large exponent
       with pytest.raises(TypeError):
        assert wrapper()== math.ldexp(1, 1000)

# Running the tests
if __name__ == '__main__':
    test = TestMathLdexp()
    test.test_positive_numbers()
    test.test_negative_numbers()
    test.test_fractional_x()
    test.test_string()
    test.test_missing()



