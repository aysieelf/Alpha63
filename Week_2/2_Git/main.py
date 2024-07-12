from dict_functions import from_string
import tuple_functions
import unittest


class TestFromString(unittest.TestCase):
    def test_basic_parsing(self):
        self.assertEqual(from_string('a=1,b=2,c=3'), {'a': '1', 'b': '2', 'c': '3'})
        self.assertEqual(from_string('a=1,b=2,c=3', value_type='int'), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(from_string('a=1.0,b=2.0,c=3.0', value_type='float'), {'a': 1.0, 'b': 2.0, 'c': 3.0})

    def test_empty_and_minimal_input(self):
        self.assertEqual(from_string(''), {})
        self.assertEqual(from_string('a=1'), {'a': '1'})

    def test_custom_separators(self):
        self.assertEqual(from_string('a:1|b:2|c:3', pair_sep='|', kv_sep=':'), {'a': '1', 'b': '2', 'c': '3'})
        self.assertEqual(from_string('key1:value1;key2:value2', pair_sep=';', kv_sep=':'), {'key1': 'value1', 'key2': 'value2'})

    def test_type_conversion_edge_cases(self):
        with self.assertRaises(ValueError):
            from_string('a=abc', value_type='int')
        with self.assertRaises(ValueError):
            from_string('a=abc', value_type='float')

    def test_missing_keys_or_values(self):
        with self.assertRaises(ValueError):
            from_string('=value')
        with self.assertRaises(ValueError):
            from_string('key=')

    def test_whitespace_handling(self):
        self.assertEqual(from_string(' a = 1 , b = 2 , c = 3 '), {' a ': ' 1 ', ' b ': ' 2 ', ' c ': ' 3 '})
        self.assertEqual(from_string(' a = 1 , b = 2 , c = 3 ', value_type='int'), {' a ': 1, ' b ': 2, ' c ': 3})

    def test_special_characters(self):
        self.assertEqual(from_string('a@=1!,b@=2!,c@=3!', pair_sep=',', kv_sep='@='), {'a': '1!', 'b': '2!', 'c': '3!'})
        self.assertEqual(from_string('key#1=value&1;key#2=value&2', pair_sep=';', kv_sep='#'), {'key#1': 'value&1', 'key#2': 'value&2'})

if __name__ == '__main__':
    unittest.main()