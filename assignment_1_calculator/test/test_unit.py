from assignment_1_calculator.BE.calculator_helper import CalculatorHelper

class TestCalculator():
    def test_first(self):
        calculator = CalculatorHelper()
        value = calculator.add(1,1)
        assert value == 2 