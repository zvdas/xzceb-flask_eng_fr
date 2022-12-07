import unittest

from translator import english_to_french, french_to_english

class MachineTranslationTest(unittest.TestCase):
    
    def test_etf(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertIsNotNone(english_to_french('Hello'))
	
    def test_fte(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertIsNotNone(french_to_english('Bonjour'))

# if __name__ == '__main__':
unittest.main()