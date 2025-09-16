from assignment_1_calculator.BE.calculator_helper import CalculatorHelper
# from assertpy import assert_that

class TestCalculator():
    def test_add(self):
        calculator = CalculatorHelper()
        value = calculator.add(1,1)
        assert value == 2 
    
    def test_subtract(self):
        calculator = CalculatorHelper()
        value = calculator.subtract(1,1)
        assert value == 0 