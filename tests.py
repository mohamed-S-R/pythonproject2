import unittest
from word_counter import count_words

class TestWordCounter(unittest.TestCase):
    def test_basic_sentences(self):
        self.assertEqual(count_words("Hello world!"), 2)
        self.assertEqual(count_words("This is a sample sentence."), 5)
        self.assertEqual(count_words("Word Counter Project"), 3)
    
    def test_empty_string(self):
        self.assertEqual(count_words("  "), 0)
    
    def test_long_sentence(self):
        self.assertEqual(count_words("Python programming is fun and powerful."), 6)

if __name__ == "__main__":
    unittest.main()