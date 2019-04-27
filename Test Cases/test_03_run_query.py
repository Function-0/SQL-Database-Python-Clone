import unittest
import squeal as a3
from equiv import equiv_tables
from database import Table, Database

class TestRunQuery(unittest.TestCase):

    def setUp(self):
        t1, t2, t3 = Table(), Table(), Table()
        t1.set_dict({'a.str': ['one', 'two', 'three', 'one'], 'a.val': ['1', '2', '3', '1'], 'a.a': ['1', '2', '3', '4']})
        t2.set_dict({'b.str': ['one', 'two', 'three', 'one'], 'b.b': ['1', '2', '3', '3'], 'b.val': ['1', '2', '3', '1']})
        t3.set_dict({'c.c': ['1', '2'], 'c.val': ['100', '200']})

        self.db = {'tablea': t1, 'tableb': t2, 'tablec': t3} 

        self.dbo = Database()
        self.dbo.set_dict(self.db)

    def test_01_single_column_unique(self):
        q = 'select a.a from tablea'
        exp = {'a.a':['1', '2', '3', '4']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "single column all unique: " + "EXPECTED: "+ str(exp) + " GOT: " + str(res)) 

    def test_02_single_column_repeats(self):
        q = 'select b.b from tableb'
        exp = {'b.b':['1', '2', '3', '3']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "single column with repeats: " + "EXPECTED: "+ str(exp) + " GOT: " + str(res)) 

    def test_03_multiple_column(self):
        q = 'select a.val,a.a from tablea'
        exp = {'a.a':['1', '2', '3', '4'], 'a.val':['1', '2', '3', '1']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "multiple columns from a single table: " + "EXPECTED: "+ str(exp) + " GOT: " + str(res)) 

    def test_04_star_column(self):
        q = 'select * from tablea'
        exp = {'a.str': ['one', 'two', 'three', 'one'], 'a.val': ['1', '2', '3', '1'], 'a.a': ['1', '2', '3', '4']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "all columns from a single table: " + "EXPECTED: "+ str(exp) + " GOT: " + str(res)) 
        
    def test_05_two_tables_one_col(self):
        q = 'select a.a from tablea,tableb'
        exp = {'a.a': ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "joined tables, single column: " + "EXPECTED: "+ str(exp) + " GOT: " + str(res)) 
        
    def test_06_two_tables_two_cols(self):
        q = 'select a.a,b.b from tablea,tableb'
        exp = {'a.a': ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4'], 
               'b.b': ['1', '2', '3', '3', '1', '2', '3', '3', '1', '2', '3', '3', '1', '2', '3', '3']}

        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "joined tables, one column per table: " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_07_two_tables_all_cols(self):
        q = 'select * from tablea,tableb'
        exp = {'b.b': ['1', '2', '3', '3', '1', '2', '3', '3', '1', '2', '3', '3', '1', '2', '3', '3'], 
               'b.str': ['one', 'two', 'three', 'one', 'one', 'two', 'three', 'one', 'one', 'two', 'three', 'one', 'one', 'two', 'three', 'one'], 
               'a.str': ['one', 'one', 'one', 'one', 'two', 'two', 'two', 'two', 'three', 'three', 'three', 'three', 'one', 'one', 'one', 'one'], 
               'b.val': ['1', '2', '3', '1', '1', '2', '3', '1', '1', '2', '3', '1', '1', '2', '3', '1'], 
               'a.val': ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '1', '1', '1', '1'], 
               'a.a': ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "joined tables, all columns: " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_08_col_eq_val(self):
        q = "select a.a from tablea where a.val='1'"
        exp = {'a.a': ['1', '4']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "selecting: where col='val': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_09_col_gt_val(self):
        q = "select a.a from tablea where a.val>'1'"
        exp = {'a.a': ['2', '3']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "selecting: where col>'val': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_10_col_eq_col(self):
        q = "select a.a from tablea where a.a=a.val"
        exp = {'a.a': ['1', '2', '3']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "selecting: where col1=col2': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_11_col_gt_col(self):
        q = "select a.a from tablea where a.a>a.val"
        exp = {'a.a': ['4']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "selecting: where col1>col2': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_12_join_col_eq_col(self):
        q = "select a.val,b.val from tablea,tableb where a.a=b.b"
        exp = {'b.val': ['1', '2', '3', '1'], 'a.val': ['1', '2', '3', '3']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "selecting from joined tables: where col1=col2': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_13_join_col_gt_col(self):
        q = "select a.val,b.val from tablea,tableb where a.a>b.b"
        exp = {'a.val': ['2', '3', '3', '1', '1', '1', '1'], 'b.val': ['1', '1', '2', '1', '2', '3', '1']}
        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "selecting from joined tables: where col1>col2': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     

    def test_14_join_multi_tables(self):
        q = "select a.val,b.val,c.val from tablea,tableb,tablec"
        exp = {'c.val': ['100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200', '100', '200'], 
               'b.val': ['1', '1', '2', '2', '3', '3', '1', '1', '1', '1', '2', '2', '3', '3', '1', '1', '1', '1', '2', '2', '3', '3', '1', '1', '1', '1', '2', '2', '3', '3', '1', '1'], 
               'a.val': ['1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1']}

        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "joining 3 tables': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))  
        
    def test_15_join_multi_tables_with_selection(self):
        q = "select a.val,b.val,c.val from tablea,tableb,tablec where a.a=b.b,a.a>c.c"
        exp = {'c.val': ['100', '100', '200', '100', '200'], 'a.val': ['2', '3', '3', '3', '3'], 'b.val': ['2', '3', '3', '1', '1']}

        res = a3.run_query(self.dbo, q).get_dict()
        self.assertTrue(equiv_tables(res, exp), "joining 3 tables with selection': " + "EXPECTED: "+ str(exp) + " GOT: " + str(res))     


if __name__ == '__main__':
    unittest.main(exit=False)

