import unittest
from reverse_word import reverse_word

class TestReverseMethods (unittest.TestCase):
    
    def test_reverse_word(self):
        self.assertEqual(reverse_word("test"), "tset")
        self.assertEqual(reverse_word("unit"), "tinu")
        self.assertEqual(reverse_word("mom"), "mom")
            
if __name__ == "__main__":
    unittest.main()
