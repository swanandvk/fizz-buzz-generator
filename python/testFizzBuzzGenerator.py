import unittest
from FizzBuzzGenerator import FizzBuzzGenerator

class FizzBuzzGeneratorTestClass(unittest.TestCase):
    		
  def test_is_valid_input(self):
    fizzbuzzgenerator = FizzBuzzGenerator()
    self.assertEquals(None,fizzbuzzgenerator.fizzBuzzGenerator(0))
    
  def test_fizz_if_input_divisible_by_3(self):
    fizzbuzzgenerator = FizzBuzzGenerator()
    self.assertEquals("fizz",fizzbuzzgenerator.fizzBuzzGenerator(3))

  def test_buzz_if_input_divisible_by_5(self):
    fizzbuzzgenerator = FizzBuzzGenerator()
    self.assertEquals("buzz",fizzbuzzgenerator.fizzBuzzGenerator(25))
  
  def test_fizzbuzz_if_input_divisible_by_3_and_5(self):
    fizzbuzzgenerator = FizzBuzzGenerator()
    self.assertEquals("fizzbuzz",fizzbuzzgenerator.fizzBuzzGenerator(15))
  
  def test_string_if_input_is_not_divisible_by_3_and_5(self):
    fizzbuzzgenerator = FizzBuzzGenerator()
    self.assertEquals("4",fizzbuzzgenerator.fizzBuzzGenerator(4))

if __name__ == '__main__':
    unittest.main()