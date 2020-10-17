import unittest as ut

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0 :
        return ("FizzBuzz")
    elif x % 3 == 0 :
        return ("Fizz")
    elif x % 5 == 0 :
        return ("Buzz")
    else : 
        return (x)


class TestFizzBuzz(ut.TestCase):
    def test_Input3SholdBeShowFizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result , "Fizz")

    def test_Input6SholdBeShowFizz(self):
        result = fizzbuzz(6)
        self.assertEqual(result , "Fizz")

    def test_Input15SholdBeShowFizzBuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result , "FizzBuzz")

    def test_Input450SholdBeShowFizzBuzz(self):
        result = fizzbuzz(450)
        self.assertEqual(result , "FizzBuzz")