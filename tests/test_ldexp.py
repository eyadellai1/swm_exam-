# tests/test_ldexp.py
from ldexp_function import tracked_ldexp, coverage_tracker
from coverage_tracker import print_coverage_report

class TestMathLdexp:
    def test_positive_numbers(self):
        assert tracked_ldexp(1, 3) == 8

    def test_negative_numbers(self):
        assert tracked_ldexp(-2, 2) == -8

    def test_fractional_x(self):
        assert tracked_ldexp(0.5, 2) == 2

    def test_zero_x(self):
        assert tracked_ldexp(0, 5) == 0

    def test_large_i(self):
        assert tracked_ldexp(1, 1000) == 2 ** 1000

if __name__ == '__main__':
    test = TestMathLdexp()
    test.test_positive_numbers()
    test.test_negative_numbers()
    test.test_fractional_x()
    test.test_zero_x()
    test.test_large_i()

    print(coverage_tracker)

