from BE.calculator_helper import CalculatorHelper
from assertpy import assert_that
import pytest
class Base():
    def setup_method(self):
        self.calculator = CalculatorHelper()

class TestCalculator(Base):
        @pytest.mark.parametrize("n1, n2, result", [(1, 1 ,2), (0, 1,1), (-4,-3,-7)])
        def test_add(self, n1, n2, result):
            assert self.calculator.add(n1, n2) == result
        @pytest.mark.parametrize("n1, n2, result", [(2, 1,1), (1,0,1), (-3,-4,1)])
        def test_subtract(self, n1, n2, result):
         assert self.calculator.subtract(n1, n2) == result
        @pytest.mark.parametrize("n1, n2, result", [(2, 4,8), (0,0,0), (-2,-4,8)])
        def test_multiply(self, n1, n2, result):
         assert self.calculator.multiply(n1, n2) == result
        @pytest.mark.parametrize("n1, n2, result", [(4, 2,2), (2,2,1), (-2,-1,2)])
        def test_divide(self, n1, n2, result):
         assert self.calculator.divide(n1, n2) == result
