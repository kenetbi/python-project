import string_utils, unittest

my_name = "kenneth"

class TestStringUtils(unittest.TestCase):
    def test_reverse(self):
        name = string_utils.reverse_string(my_name)
        self.assertEqual(name, "htennek")
        self.assertTrue(name == "htennek")

    def test_is_capital(self):
        name = string_utils.capitalize_string(my_name)
        self.assertEqual(name[0], "K")
        self.assertTrue(string_utils.is_capitalized(name))

if __name__ == "__main__":
    unittest.main()