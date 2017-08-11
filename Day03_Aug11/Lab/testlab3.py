import unittest
from lab3ANSWERS import *

class TestStringMethods(unittest.TestCase):

    def test_shout(self):
        self.assertEqual(shout('Hello.'), 'HELLO!')
    def test_reverse(self):
        self.assertEqual(reverse('Name'), 'emaN')
    def test_reversewords(self):
        self.assertEqual(reversewords('Hello world!'), 'world! Hello')
    def test_reversewordletters(self):
        self.assertEqual(reversewordletters('Hello world!'), '!dlrow olleH')


if __name__ == '__main__':
    unittest.main()
