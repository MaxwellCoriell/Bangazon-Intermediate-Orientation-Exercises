# Calculator Unit Tests

# Just like you did in JavaScript when you learned about Jasmine, you're going to create a class that test the functionality of a Calculator class.

##### Starter code for calculator class

class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number, number)
    """

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """
        # return 9
        return firstOperand + secondOperand

    def subtract(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """
        # return -5
        return firstOperand - secondOperand

    def multiply(self, firstOperand, secondOperand):
        """Multiplies two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """
        # return 14
        return firstOperand * secondOperand

    def divide(self, firstOperand, secondOperand):
        """Divides one number from another

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """
        # return 0.2857
        return firstOperand / secondOperand

## Running the test class

# ```
# python test_calc.py -v
# ```