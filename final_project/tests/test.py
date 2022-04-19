import unittest

from machinetranslation.translator import french_to_english, english_to_french


class TestTranslator(unittest.TestCase): 

    def test_f2e_null(self): 
        self.assertEqual(french_to_english(), None)  # Test F2E Null

    def test_f2e_notnull(self): 
        self.assertEqual(french_to_english("Bonjour"),"Hello")  # Test F2E Word

    def test_e2f_null(self): 
        self.assertEqual(english_to_french(), None)  # Test E2F Null

    def test_e2f_notnull(self): 
        self.assertEqual(english_to_french("Hello"),"Bonjour")  # Test E2F Word


