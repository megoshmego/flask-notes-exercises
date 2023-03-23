# first need to specify the imports. This is an example of a unittest of 
# algorithms.py

from unittest import TestCase
from algorithms import reverse_str, is_palindrome, factorial


class AlgorithmsTestCase(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str('hello'), 'olleh')
        self.assertEqual(reverse_str('Apple'), 'elppA')

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('kayak'))
        self.assertFalse(is_palindrome('taco'))
        # the above IS case sensitive. to make it equal regardless of case
        # insert into algorithms.py 's.lower()' == rev.lower()

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

        # because the algorithms code already raises a ValueError if a number is not an 
        # integer or is negative BUT there is a solution. assertRaises()

        self.assertRaises(ValueError, factorial(-5))

        # this will break the code because it raises an exception.
        # or we can actually call the function

        self.assertRaises(ValueError, factorial, -5)

        # ValueError - the type of exception we are expecting
        # factorial - the callable, or function you want to call 
        # -5 - the argument we are passing into the callable



# tool in VSCODE to run tests
# open the command pallete (Ctrl + Shift + P)
# search for tests, select 'Python: Run All Tests'
# if the tool has not been configured, configure to 'unittest'
# note the folder the unittests are in, select 'Root Directory', select how tests have 
#   been labeled. select 'test_'. then test will run, a special tab pops up with the 
#   tested folders. click 'play arrow' icon. green check means it works. if output is a 
#   red arrow, click on the above icon that is a box with an arrow, as it will give 
#   more detail on what passed and failed 
  

 
