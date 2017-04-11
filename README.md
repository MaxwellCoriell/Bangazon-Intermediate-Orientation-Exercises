# Orientation Exercises For Python
This is a suggested order for completing the exercises in orientation:

## [Intermediate exercises](./intermediate_orientation)
1. [Family Dictionary](./family_dict.py)
1. [Kill Nickelback](./nickleback.py)
1. [RandomSquared](random_squared.py)
1. [Test Animals](./test-animals/)
1. [Calculator](./test_calc/)

|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---

# The Family Dictionary

## Setup

```
mkdir -p ~/workspace/python/exercises/family_dictionary && cd $_
touch family_dict.py
```

## Instructions

1. Define a dictionary that contains information about several members of your family. Use the following example as a template.
    ```
    my_family = {
        'sister': {
            'name': 'Krista',
            'age': 42
        },
        'mother': {
            'name': 'Cathie',
            'age': 70
        }
    }
    ```
2. Using a dictionary comprehension, produce output that looks like the following example.
    ```
    Krista is my sister and is 42 years old
    ```

    > **Helpful hint:** To convert an integer into a string in Python, it's `str(integer_value)`

|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---

# Kill Nickelback

In this exercises, you're going to use a conditional statement inside a comprehension. Let's look at a basic example.

```python
nums = range(10)
small_numbers = [num for num in nums if num < 6]
# Only add numbers to the new list if the value is less than 6

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [ word.title() for word in words if len(word) == 3 ]
# len(stringVariable) is equivalent to stringVariable.length in JavaScript
```

## Setup

```
mkdir -p ~/workspace/python/exercises/sets && cd $_
touch nickelback.py
```

## Instructions

1. Define a set that contains tuples. Each tuple should contain two strings:
    1. The name of an artist
    1. A song by that artist

    Make sure that some of the songs are from the band Nickelback. You can see a [list of their greatest hits](https://www.amazon.com/Best-Nickelback-1/dp/B00FFERTUK/) on Amazon.
    ```
    # Example set
    songs = {
        ('Nickelback', 'How You Remind Me'), 
        ('Will.i.am', 'That Power'),
        ('Miles Davis', 'Stella by Starlight'),
        ('Nickelback', 'Animals')
    }
    ```
2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---

# Squared Randoms

## Setup

```
mkdir -p ~/workspace/python/exercises/lists && cd $_
touch random_squared.py
```

## References

* [Random module](https://docs.python.org/3.6/library/random.html)
* [Python Lists](https://docs.python.org/3.6/tutorial/datastructures.html)

## Instructions

1. Using the `random` module and the `range` method, generate a list of 20 random numbers between 0 and 49.
    ```
    import random

    random_numbers = [...insert awesome code here...]
    print(random_numbers)
    ```
2. With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is `[2, 5]`, the final list will be `[4, 25]`.

|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---

# Testing the Animals

> **Note:** This code exercise will be part of a live coding session with the instructor. Feel free to try it on your own beforehand and come to class with questions, or just wait until live coding starts.

## Setup

```
mkdir -p ~/workspace/python/exercises/testing && cd $_
touch animals.py
```

1. Copy the contents of [animals.py](./assets/animal.py) into the file you just created.

## Overview

As a team, we'll be building unit test coverage for all the functionality of the code in the `animal` module. We'll discuss how writing tests often affect the implementation code, and how to think bout covering edge cases in your test suit.

## Instructions

Write test cases to verify the I/O of the following methods of `Animal` and `Dog`.

1. In the test class' `setUpClass()` method, create an instance of `Animal` and `Dog`.
1. Animal object has the correct `name` property.
1. Set a species and verify that the object property of `species` has the correct value.
1. Invoking the `walk()` method set the correct speed on the both objects.
1. The animal object is an instance of `Animal`.
1. The dog object is an instance of `Dog`.

## Test Discovery

Read the [Test Discovery section](https://docs.python.org/3.3/library/unittest.html#unittest-test-discovery) of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.

```
python -m unittest discover -s . -p "Test*.py" -v
```


|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---

# Calculator Unit Tests

Just like you did in JavaScript when you learned about Jasmine, you're going to create a class that test the functionality of a Calculator class.

##### Starter code for test class

> **Note**: The [`setUpClass`](https://docs.python.org/3.6/library/unittest.html#unittest.TestCase.setUpClass) method below must have the `@classmethod` decorator above it. 

```python
import unittest
import calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)

  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
```

##### Starter code for calculator class

```python
class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        return firstOperand + secondOperand
```

## Running the test class

```
python CalcTest.py -v
```