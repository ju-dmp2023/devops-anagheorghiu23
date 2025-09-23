from BE.calculator_helper import CalculatorHelper
from assertpy import assert_that
import pytest
    
class TestCalculator():
    # @classmethod
    # def setup(cls):
    #     calculator = CalculatorHelper()


    # @classmethod
    # def teardown_class(cls):
    #     calculator = CalculatorHelper()

#Assert

        @pytest.mark.parametrize("n,expected", [(1, 2), (0, 1), (-4,-3)])
        def test_add(self, n, expected):
         assert n + 1 == expected
        @pytest.mark.parametrize("n,expected", [(2, 1), (1, 0), (-3,-4)])
        def test_subtract(self, n, expected):
         assert n - 1 == expected
        @pytest.mark.parametrize("n,expected", [(2, 4), (0, 0), (-2,-4)])
        def test_multiply(self, n, expected):
         assert n * 2 == expected
        @pytest.mark.parametrize("n,expected", [(2, -4), (0, 0), (-2,4)])
        def test_multiply_negative(self, n, expected):
         assert n * -2 == expected
        @pytest.mark.parametrize("n,expected", [(4, 2), (0, 0), (-2,-1)])
        def test_divide(self, n, expected):
         assert n / 2 == expected
  
    # def test_add(self):
    #     calculator = CalculatorHelper()
    #     value = calculator.add(1,-1)
    #     assert_that(value).is_equal_to(0)

    # def test_subtract(self):
    #     calculator = CalculatorHelper()
    #     value = calculator.subtract(1,1)
    #     assert_that(value).is_equal_to(0)