import unittest

import squeal as a3
from database import *
import equiv

class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_01_cartesian_product_one_col_one_row(self):
        t1 = Table()
        t1.set_dict({'a': ['b']})
        t2 = Table()
        t2.set_dict({'c': ['d']})

        expected = {'a': ['b'], 'c': ['d']}
        res = a3.cartesian_product(t1, t2)
        self.assertTrue(equiv.equiv_tables(res.get_dict(), expected), "one column one row")

    def test_02_cartesian_product_two_col_one_row(self):
        t1 = Table()
        t1.set_dict({'a': ['b'], 'x': ['y']})
        t2 = Table()
        t2.set_dict({'c': ['d']})

        expected = {'a': ['b'], 'c': ['d'], 'x': ['y']}
        res = a3.cartesian_product(t1, t2)
        self.assertTrue(
            equiv.equiv_tables(res.get_dict(), expected), "two columns in first table, one row")

    def test_03_cartesian_product_two_col2_one_row(self):
        t1 = Table()
        t1.set_dict({'a': ['b'], 'x': ['y']})
        t2 = Table()
        t2.set_dict({'c': ['d']})

        expected = {'a': ['b'], 'c': ['d'], 'x': ['y']}
        res = a3.cartesian_product(t2, t1)
        self.assertTrue(
            equiv.equiv_tables(res.get_dict(), expected), "two columns in second table, one row")

    def test_04_cartesian_product_two_col_two_row(self):
        t1 = Table()
        t1.set_dict({'a': ['b', 'c'], 'x': ['y', 'z']})
        t2 = Table()
        t2.set_dict({'d': ['e', 'f'], 'u': ['v', 'w']})
        expected = {'a': ['b', 'c', 'b', 'c'], 'x': ['y', 'z', 'y', 'z'],
                    'd': ['e', 'e', 'f', 'f'], 'u': ['v', 'v', 'w', 'w']}
        res = a3.cartesian_product(t2, t1)
        self.assertTrue(equiv.equiv_tables(res.get_dict(), expected), "two columns two rows")

    def test_05_cartesian_product_two_col_two_three_row(self):
        t1 = Table()
        t1.set_dict({'a': ['b', 'c', 'q'], 'x': ['y', 'z', 'r']})
        t2 = Table()
        t2.set_dict({'d': ['e', 'f'], 'u': ['v', 'w']})
        expected = {
            'a': ['b', 'c', 'q', 'b', 'c', 'q'],
            'x': ['y', 'z', 'r', 'y', 'z', 'r'],
            'd': ['e', 'e', 'e', 'f', 'f', 'f'],
            'u': ['v', 'v', 'v', 'w', 'w', 'w']}
        res = a3.cartesian_product(t1, t2)
        self.assertTrue(
            equiv.equiv_tables(res.get_dict(), expected), "two columns three rows in table1")

    def test_06_cartesian_product_two_col_three_three_row(self):
        t1 = Table()
        t1.set_dict({'a': ['b', 'c', 'q'], 'x': ['y', 'z', 'r']})
        t2 = Table()
        t2.set_dict({'d': ['e', 'f', 'l'], 'u': ['v', 'w', 'm']})
        expected = {
            'a': ['b', 'c', 'q', 'b', 'c', 'q', 'b', 'c', 'q'],
            'x': ['y', 'z', 'r', 'y', 'z', 'r', 'y', 'z', 'r'],
            'd': ['e', 'e', 'e', 'f', 'f', 'f', 'l', 'l', 'l'],
            'u': ['v', 'v', 'v', 'w', 'w', 'w', 'm', 'm', 'm']}
        res = a3.cartesian_product(t1, t2)
        self.assertTrue(equiv.equiv_tables(res.get_dict(), expected), "two columns three rows")

    def test_07_cartesian_product_one_col_three_six_row(self):
        t1 = Table()
        t1.set_dict({'a': ['b', 'c', 'd']})
        t2 = Table()
        t2.set_dict({'e': ['f', 'g', 'h', 'i', 'j', 'k']})
        expected = {
            'a': ['b', 'c', 'd', 'b', 'c', 'd', 'b', 'c', 'd', 'b', 'c', 'd', 'b', 'c', 'd', 'b', 'c', 'd'],
            'e': ['f', 'f', 'f', 'g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i', 'j', 'j', 'j', 'k', 'k', 'k']}
        res = a3.cartesian_product(t1, t2)
        self.assertTrue(
            equiv.equiv_tables(res.get_dict(), expected), "two columns three and six rows")

    def test_08_cartesian_product_zero_rows(self):
        t1 = Table()
        t1.set_dict({'a': []})
        t2 = Table()
        t2.set_dict({'e': []})
        expected = {'a': [], 'e': []}
        res = a3.cartesian_product(t1, t2)
        self.assertTrue(equiv.equiv_tables(res.get_dict(), expected), "no data rows")

    def test_09_cartesian_product_zero_one_rows(self):
        t1 = Table()
        t1.set_dict({'a': []})
        t2 = Table()
        t2.set_dict({'e': ['f']})
        expected = {'a': [], 'e': []}
        res = a3.cartesian_product(t1, t2)
        self.assertTrue(equiv.equiv_tables(res.get_dict(), expected), "no rows and one row")

    def test_99_cartesian_product_mutable(self):
        t1 = Table()
        t1.set_dict({'a': ['b', 'c'], 'x': ['y', 'z']})
        t1copy = {'a': ['b', 'c'], 'x': ['y', 'z']}
        t2 = Table()
        t2.set_dict({'d': ['e', 'f'], 'u': ['v', 'w']})
        t2copy = {'d': ['e', 'f'], 'u': ['v', 'w']}
        a3.cartesian_product(t2, t1)
        self.assertEqual(t1.get_dict(), t1copy, "t1 should not be modified")
        self.assertEqual(t2.get_dict(), t2copy, "t1 should not be modified")


if __name__ == '__main__':
    unittest.main()
