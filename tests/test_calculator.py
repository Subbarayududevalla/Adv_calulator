import pytest
# Import the Calculator class from the calculator package
from proj_cal.calculator import Calculator
# Define the test function
def test_calculator():
    # Use the pytest module to test the calculator

    # Create a fixture that will provide a calculator instance for each test case
    @pytest.fixture
    def Calc():
        return Calculator()

    # Test the add method
    def test_add(Calc):
        # Check if the add method returns the correct sum
        assert Calc.add(2, 3) == 5
        assert Calc.add(-1, 4) == 3
        assert Calc.add(0, 0) == 0
        # Check if the add method raises a ValueError exception for invalid input
        with pytest.raises(ValueError):
            Calc.add("a", 1)
        with pytest.raises(ValueError):
            Calc.add(1, "b")

    # Test the subtract method
    def test_subtract(Calc):
        # Check if the subtract method returns the correct difference
        assert Calc.subtract(5, 3) == 2
        assert Calc.subtract(-1, 4) == -5
        assert Calc.subtract(0, 0) == 0
        # Check if the subtract method raises a ValueError exception for invalid input
        with pytest.raises(ValueError):
            Calc.subtract("a", 1)
        with pytest.raises(ValueError):
            Calc.subtract(1, "b")

    # Test the multiply method
    def test_multiply(Calc):
        # Check if the multiply method returns the correct product
        assert Calc.multiply(2, 3) == 6
        assert Calc.multiply(-1, 4) == -4
        assert Calc.multiply(0, 0) == 0
        # Check if the multiply method raises a ValueError exception for invalid input
        with pytest.raises(ValueError):
            Calc.multiply("a", 1)
        with pytest.raises(ValueError):
            Calc.multiply(1, "b")

    # Test the divide method
    def test_divide(Calc):
        # Check if the divide method returns the correct quotient
        assert Calc.divide(6, 3) == 2
        assert Calc.divide(-6, 3) == -2
        assert Calc.divide(6, -3) == -2
        assert Calc.divide(-6, -3) == 2
        assert Calc.divide(0, 3) == 0
        # Check if the divide method raises a ZeroDivisionError exception for zero denominator
        with pytest.raises(ZeroDivisionError):
            Calc.divide(6, 0)
        # Check if the divide method raises a ValueError exception for invalid input
        with pytest.raises(ValueError):
            Calc.divide("a", 1)
        with pytest.raises(ValueError):
            Calc.divide(1, "b")