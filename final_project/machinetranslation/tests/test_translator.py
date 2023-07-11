import unittest
from ..translator import english_to_french, french_to_english


class TranslationTestCase(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hi"), "Bonjour")
        self.assertEqual(english_to_french("Home"), "Accueil")
        self.assertNotEqual(english_to_french("mismatch"), "déviation")
        self.assertNotEqual(english_to_french("tower"), "tour")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Accueil"), "Home")
        self.assertNotEqual(english_to_french("déviation"), "drift")
        self.assertNotEqual(english_to_french("la tour"), "round")


if __name__ == '__main__':
    unittest.main()