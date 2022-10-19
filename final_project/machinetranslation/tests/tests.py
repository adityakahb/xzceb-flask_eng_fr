"""
    Tests file to test the translator functionality
"""
import unittest
from translator import english_to_french
from translator import french_to_english


class TestLanguageTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(
            None), 'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(
            None), 'Hello')


if __name__ == '__main__':
    unittest.main()
