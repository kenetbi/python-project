import unittest

def add(a,b):
   return a+b

class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = add(1,2)
        expected_result = 3
        self.assertEqual(result, expected_result) #test if two values are equal

    def test_string_length(self):
        text = "Hello, World!"
        self.assertEqual(len(text), 13) # test if two values are equal

    def test_contains(self):
        text = "Hello, World!"
        self.assertTrue("Hello" in text) # test boolean condition
        self.assertFalse("@" in text)

    def test_in(self):
        special = ["!","@","#","$"]
        self.assertIn("!", special) # test if value is in the collection
        self.assertNotIn("*", special)



if __name__ == "__main__":
    unittest.main()