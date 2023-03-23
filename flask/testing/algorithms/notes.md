# FLASK TESTING

## UNIT TESTS 

test one "unit" of functionality
    typically one function or method 

Don't test integration of components
    like flask

promotes modular code 


## ASSERT
    expecting something that you know to be true. if it does not come back true it will raise 
    an error 

                loosely stated

                if not condition:
                    raise AssertionError 

  
        Example 

            def adder(x, y):
                """ Add two numbers together """

                return x + y

            USE THE FOLLOWING IN PYTHON IN TERMINAL

            assert adder(2, 5) == 7


            The code will STOP if the assertion fails, and does not produce any 
            kind of report. can be disabled if using python '-O name_of_file.py'

    
    ASSERT IS A STATEMENT NOT A FUNCTION 

## DOCTESTS 

    easiest way to run these tests is by testing inside of python terminal

    example. 

    _$ python_ 

    >> from arithmetic_dt import adder
    >> adder(3,5)
    8
    

    must be INCLUDED in doctest app 

            *def adder(x, y):
                """
                Adds two numbers together.
                >>> adder(3,5)
                8
                >>> adder(-1, 50)
                49
                """

                return x + y*

    if the doctest app is ran in ipython, this will be included when using help()

    HOW TO RUN 

    _$ python -m doctest arithmetic.py_
    _$ (nothing output for success)_

        OR run in verbose to get more detail information 

        _$ python -m doctest -v arithmetic.py_

    tests aren't all written within the docstring because it makes the code ugly 

## UNITTESTING 

    create seperate classes for testing in a seperate file 

        *from unittest import TestCase 

        class AdditionTestCase(TestCase):
            """ Examples of unit tests """

            def test_adder(self):
                assert arithmetic.adder(2,3) == 5*

    
    Tests are a bundle of tests 
        in a class that subclasses TestCase

        Test files must start with test_ 

        _python -m unittest NAME_OF_FILE_ runs all cases 


    Gives access to more specific Assert testing 

        """Example of unit tests"""

        *import arithmetic
        from unittest import TestCase

        class AdditionTestCase(TestCase):
            """Examples of unit tests"""

            def test_adder(self):
                assert arithmetic.adder(2, 3) == 5

            def test_adder_2(self):
                #instead of assert arithmetic.adder(2, 2) == 4
                self.assertEqual(arithmetic.adder(2, 2), 4)
                self.assertEqual(arithmetic.adder(40, 50), 90)*

            
        $ python -m unittest tests_arithmetic.py


        IF we ran the above code asserEqual returns more details 

        BOTH of the 'test_adder' are considered two tests only, no matter how many 
        statements are in it. 

    
    # The file 'algorithms' is a demo of unit testing  

    



