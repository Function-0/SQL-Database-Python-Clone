import unittest
import reading as a3
import equiv

class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_01_read_table_single_col_single_row(self):
        p1 = 'single_single.csv'
        r = a3.read_table(p1)
        d = {'a.test': ['A']}
        e = equiv.equiv_tables(r.get_dict(), d)
        self.assertTrue(e, "table with one column, one row")

    def test_02_read_table_single_col_multi_row(self):
        p1 = 'single_multi.csv'
        r = a3.read_table(p1)
        d = {'a.test': ['A', 'B']}
        e = equiv.equiv_tables(r.get_dict(), d)
        self.assertTrue(e, "table with one column, multiple rows")

    def test_03_read_table_multi_col_single_row(self):
        p1 = 'multi_single.csv'
        r = a3.read_table(p1)
        d = {'a.test': ['A'], 'b.test': ['B']}
        e = equiv.equiv_tables(r.get_dict(), d)
        self.assertTrue(e, "table with multiple columns, single row")

    def test_04_read_table_multi_col_multi_row(self):
        p1 = 'multi_multi.csv'
        r = a3.read_table(p1)
        d = {'a.test': ['A1', 'A2'], 'b.test': ['B1', 'B2']}
        e = equiv.equiv_tables(r.get_dict(), d)
        self.assertTrue(e, "table with multiple columns, multiple rows")

    def test_05_read_table_single_col_no_rows(self):
        p1 = 'single_none.csv'
        r = a3.read_table(p1)
        d = {'a.test': []}
        e = equiv.equiv_tables(r.get_dict(), d)
        self.assertTrue(e, "table with one column, no rows")

    def test_06_read_table_multi_col_no_rows(self):
        p1 = 'multi_none.csv'
        r = a3.read_table(p1)
        d = {'a.test': [], 'b.test': []}
        e = equiv.equiv_tables(r.get_dict(), d)
        self.assertTrue(e, "table with multiple column, no rows")

    def test_07_read_table_multi_col_multi_rows_diff_col_names(self):
        p1 = 'multi_multi_colnames.csv'
        r = a3.read_table(p1)
        d = {'atest': ['A1', 'A2'], 'btest': ['B1', 'B2']}
        e = equiv.equiv_tables(r.get_dict(), d)
        self.assertTrue(
            e,
            "table with multiple columns, multiple rows, column names not following letter.string format")

if __name__ == '__main__':
    unittest.main(exit=False)
