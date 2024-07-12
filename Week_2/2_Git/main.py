from dict_functions import aggregate_min
import tuple_functions

import unittest


class TestAggregateMinFunction(unittest.TestCase):
    def test_basic_aggregation(self):
        self.assertEqual(aggregate_min([('a', 1), ('b', 2), ('c', 3)]), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(aggregate_min([('a', 1), ('b', 2), ('a', 0)]), {'a': 0, 'b': 2})

    def test_empty_and_minimal_input(self):
        self.assertEqual(aggregate_min([]), {})
        self.assertEqual(aggregate_min([('a', 1)]), {'a': 1})

    def test_mixed_data_types(self):
        self.assertEqual(aggregate_min([('a', 1), ('b', 2.5), ('a', 0.5)]), {'a': 0.5, 'b': 2.5})
        self.assertEqual(aggregate_min([('a', 1.0), ('b', 2), ('a', 0)]), {'a': 0, 'b': 2})

    def test_non_comparable_values(self):
        with self.assertRaises(TypeError):
            aggregate_min([('a', 'string'), ('a', 1)])

    def test_special_characters(self):
        self.assertEqual(aggregate_min([('a$', 3), ('b@', 2), ('a$', 1)]), {'a$': 1, 'b@': 2})
        self.assertEqual(aggregate_min([('key&', 4), ('key&', 2)]), {'key&': 2})

    def test_negative_and_zero_values(self):
        self.assertEqual(aggregate_min([('a', -1), ('b', 0), ('a', -3)]), {'a': -3, 'b': 0})
        self.assertEqual(aggregate_min([('x', -5), ('y', -2), ('x', 0)]), {'x': -5, 'y': -2})

if __name__ == '__main__':
    unittest.main()

