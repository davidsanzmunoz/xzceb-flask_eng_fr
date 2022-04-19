import unittest

#from translator import french_to_english, english_to_french
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f_null(self):
        self.assertNotEqual(english_to_french("None"), '')
    def test_e2f_notequal(self):
        self.assertNotEqual(english_to_french(0), 0)
    def test_e2f_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_f2e_null(self):
        self.assertNotEqual(french_to_english("None"), '')
    def test_f2e_notequal(self):
        self.assertNotEqual(french_to_english(0), 0)
    def test_f2e_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()    	
