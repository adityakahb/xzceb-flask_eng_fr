"""
    Tests file to test the translator functionality
"""
import unittest
from translator import french_to_english
from translator import english_to_french


class TestLanguageTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(
            None), 'Could not process English Text')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(
            None), 'Could not process French Text')


if __name__ == '__main__':
    unittest.main()
