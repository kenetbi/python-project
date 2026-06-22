import unittest

class MyTestCase(unittest.TestCase):
    def test_word(self):
        text = 2134
    
        with self.assertRaises(TypeError):
            self.assertIn("World", text)

if __name__ == "__main__":
  unittest.main()