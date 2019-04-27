# NOTE TO TA: DO NOT MIND THE LONG PROCCESSING TIMES. THIS PROGRAM MAY BE
# INEFFICIENT, BUT I ASSURE YOU THAT THIS PROGRAM WILL PROCESS THE REQUESTED
# QUERY... EVENTUALLY
# ==========================================================================
from reading import *
from database import *
import time
# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results

# Everything below here is used to test cartesian_product
# Univeral Empty Dictionary
empty_table = dict()
# Dictionaries with one row and with variable headers
A_table_1 = {"Colours": ["Black"]}
A_table_2 = {"Fruits": ["Banana"], "Weapon": ["Axe"], "Sweets": ["Ice-cream"],
             "Air": ["Polluted"], "Math": ["Addition"]}
A_table_3 = {"Letters": ["A"]}
A_table_4 = {"Life": ["Death"], "Plant": ["Plant"], "Probability": ["77.894"],
             ">?/.?>?": ["#@)(*$#  "], "             ": ["       hi"]}
# Dictionaries with one header and with variable rows
B_table_1 = {"Stuff": ["Banana", "Weapon", "Axe", "Sweets", "Ice-cream"]}
B_table_2 = {"Life": [
    "77.894", ">?/.?>?", "#@)(*$#  ", "             ", "       hi"]}
# Dictionaries with variable rows and with variable headers
C_table_1 = {"Pencil": ["Paper", "Sharpener", "Ruler"],
             "Time": ["Travel", "Regression", "Age"],
             "Fight": ["Mercy", "Spare", "Betray"]}
C_table_2 = {"Fail": ["[]", ' ', "%"],
             "545": ["6 + 3", "FSG", "\_/"],
             "Soup": ["Food", "Bowl", "Drop"]}


def cartesian_product(table_1, table_2):
    '''(Table, Table) -> Table
    Given two different tables, table_1 and table_2: Returns the Cartesian
    product of the two tables.
    REQ: table_1, table_2 are non-empty
    >>> t1 = Table()
    >>> t2 = Table()
    >>> result = cartesian_product(t1, t2)
    >>> result_dict = result.get_dict()
    >>> expected = {}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(A_table_1)
    >>> t2.set_dict(empty_table)
    >>> result = cartesian_product(t1, t2)
    >>> result_dict = result.get_dict()
    >>> expected = {'': [], 'Colours': []}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(A_table_1)
    >>> t2.set_dict(empty_table)
    >>> result = cartesian_product(t2, t1)
    >>> result_dict = result.get_dict()
    >>> expected = {'': [], 'Colours': []}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(A_table_3)
    >>> t2.set_dict(A_table_1)
    >>> result = cartesian_product(t1, t2)
    >>> result_dict = result.get_dict()
    >>> expected = {"Letters": ["A"], "Colours": ["Black"]}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(A_table_3)
    >>> t2.set_dict(A_table_1)
    >>> result = cartesian_product(t2, t1)
    >>> result_dict = result.get_dict()
    >>> expected = {"Letters": ["A"], "Colours": ["Black"]}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(A_table_2)
    >>> t2.set_dict(A_table_4)
    >>> result = cartesian_product(t1, t2)
    >>> result_dict = result.get_dict()
    >>> expected = ({'Math': ['Addition'], 'Plant': ['Plant'],
    ... 'Sweets': ['Ice-cream'], 'Fruits': ['Banana'], 'Weapon': ['Axe'],
    ... '>?/.?>?': ['#@)(*$#  '], 'Air': ['Polluted'],
    ... '             ': ['       hi'], 'Life': ['Death'],
    ... 'Probability': ['77.894']})
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(A_table_2)
    >>> t2.set_dict(A_table_4)
    >>> result = cartesian_product(t2, t1)
    >>> result_dict = result.get_dict()
    >>> expected = {'Life': ['Death'], 'Air': ['Polluted'],
    ... 'Math': ['Addition'], 'Weapon': ['Axe'], 'Sweets': ['Ice-cream'],
    ... '             ': ['       hi'], '>?/.?>?': ['#@)(*$#  '],
    ... 'Probability': ['77.894'], 'Plant': ['Plant'], 'Fruits': ['Banana']}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(C_table_1)
    >>> t2.set_dict(C_table_2)
    >>> result = cartesian_product(t1, t2)
    >>> result_dict = result.get_dict()
    >>> expected = {'Fight': ['Mercy', 'Mercy', 'Mercy', 'Spare',
    ... 'Spare', 'Spare', 'Betray', 'Betray', 'Betray'],
    ... 'Fail': ['[]', ' ', '%', '[]', ' ', '%', '[]', ' ', '%'],
    ... 'Pencil': ['Paper', 'Paper', 'Paper', 'Sharpener', 'Sharpener',
    ... 'Sharpener', 'Ruler', 'Ruler', 'Ruler'], '545': ['6 + 3', 'FSG',
    ... '\\_/', '6 + 3', 'FSG', '\\_/', '6 + 3', 'FSG', '\\_/'],
    ... 'Soup': ['Food', 'Bowl', 'Drop', 'Food', 'Bowl', 'Drop', 'Food',
    ... 'Bowl', 'Drop'], 'Time': ['Travel', 'Travel', 'Travel',
    ... 'Regression', 'Regression', 'Regression', 'Age', 'Age', 'Age']}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(C_table_1)
    >>> t2.set_dict(C_table_2)
    >>> result = cartesian_product(t2, t1)
    >>> result_dict = result.get_dict()
    >>> expected = {'Time': ['Travel', 'Regression', 'Age', 'Travel',
    ... 'Regression', 'Age', 'Travel', 'Regression', 'Age'], 'Soup': ['Food',
    ... 'Food', 'Food', 'Bowl', 'Bowl', 'Bowl', 'Drop', 'Drop', 'Drop'],
    ... 'Pencil': ['Paper', 'Sharpener', 'Ruler', 'Paper', 'Sharpener',
    ... 'Ruler', 'Paper', 'Sharpener', 'Ruler'], 'Fail': ['[]', '[]', '[]',
    ... ' ', ' ', ' ', '%', '%', '%'], 'Fight': ['Mercy', 'Spare', 'Betray',
    ... 'Mercy', 'Spare', 'Betray', 'Mercy', 'Spare', 'Betray'],
    ... '545': ['6 + 3', '6 + 3', '6 + 3', 'FSG', 'FSG', 'FSG', '\\_/',
    ... '\\_/', '\\_/']}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(B_table_1)
    >>> t2.set_dict(B_table_2)
    >>> result = cartesian_product(t1, t2)
    >>> result_dict = result.get_dict()
    >>> expected = {'Stuff': ['Banana', 'Banana', 'Banana', 'Banana',
    ... 'Banana', 'Weapon', 'Weapon', 'Weapon', 'Weapon', 'Weapon', 'Axe',
    ... 'Axe', 'Axe', 'Axe', 'Axe', 'Sweets', 'Sweets', 'Sweets', 'Sweets',
    ... 'Sweets', 'Ice-cream', 'Ice-cream', 'Ice-cream', 'Ice-cream',
    ... 'Ice-cream'], 'Life': ['77.894', '>?/.?>?', '#@)(*$#  ',
    ... '             ', '       hi', '77.894', '>?/.?>?', '#@)(*$#  ',
    ... '             ', '       hi', '77.894', '>?/.?>?', '#@)(*$#  ',
    ... '             ', '       hi', '77.894', '>?/.?>?', '#@)(*$#  ',
    ... '             ', '       hi', '77.894', '>?/.?>?', '#@)(*$#  ',
    ... '             ', '       hi']}
    >>> result_dict == expected
    True

    >>> t1 = Table()
    >>> t2 = Table()
    >>> t1.set_dict(B_table_1)
    >>> t2.set_dict(B_table_2)
    >>> result = cartesian_product(t2, t1)
    >>> result_dict = result.get_dict()
    >>> expected = {'Life': ['77.894', '77.894', '77.894', '77.894',
    ... '77.894', '>?/.?>?', '>?/.?>?', '>?/.?>?', '>?/.?>?', '>?/.?>?',
    ... '#@)(*$#  ', '#@)(*$#  ', '#@)(*$#  ', '#@)(*$#  ', '#@)(*$#  ',
    ... '             ', '             ', '             ', '             ',
    ... '             ', '       hi', '       hi', '       hi', '       hi',
    ... '       hi'], 'Stuff': ['Banana', 'Weapon', 'Axe', 'Sweets',
    ... 'Ice-cream', 'Banana', 'Weapon', 'Axe', 'Sweets', 'Ice-cream',
    ... 'Banana', 'Weapon', 'Axe', 'Sweets', 'Ice-cream', 'Banana',
    ... 'Weapon', 'Axe', 'Sweets', 'Ice-cream', 'Banana', 'Weapon', 'Axe',
    ... 'Sweets', 'Ice-cream']}
    >>> result_dict == expected
    True
    '''
    # Obtain table_1's name
    table_1_name = table_1.get_table_name()
    # Obtain table_2's name
    table_2_name = table_2.get_table_name()
    # Obtain table_1's column names
    table_1_headers = table_1.get_column_names()
    # Obtain table_2's column names
    table_2_headers = table_2.get_column_names()
    # Obtain table_1's rows
    table_1_rows = table_1.get_rows()
    # Obtain table_2's rows
    table_2_rows = table_2.get_rows()
    # Create a Table object
    cartesian_product_table = Table()
    # Set the Table object's name as the combined names of table_1 and table_2,
    # seperated with the token ','
    cartesian_product_table.set_table_name(table_1_name + ',' + table_2_name)
    # Set the Table object's column names be the combined column names of
    # table_1 and table_2
    cartesian_product_table.set_column_names(table_1_headers + table_2_headers)
    # Go through each row in table_1
    for table_1_row in table_1_rows:
        # Go through each row in table_2
        for table_2_row in table_2_rows:
            # Combine the current table_1 row with the current table_2 row
            table_product = table_1_row + table_2_row
            # Add the new row to the new table object
            cartesian_product_table.add_row(table_product)
    # Returns the Cartesian product table
    return cartesian_product_table


# Private helper function
def _parse_query(query):
    '''(str) ->  dict of {str: list of str}
    Given a query to process: Returns a dictionary with three entries. Each
    entry has a key that represents one of the three keywords possible in the
    query, and a value of a list of tokens which relates directly to its
    specified keyword.
    REQ: query restricted to the following format:
        |select <token> from <token> where <token>|
        - Where each additional token is seperated by ','
        - No spaces are allowed to be in the token, or beside the token
        - The keyword "where" is optional for the query
    REQ: query is non-empty
    >>> query = "select * from seinfeld-foods,seinfeld-episodes where\
    ... e.food=f.food"
    >>> test = _parse_query(query)
    >>> test == {'from': ['seinfeld-foods', 'seinfeld-episodes'],
    ... 'where': ['e.food=f.food'], 'select': ['*']}
    True

    >>> query = "select i.rating,l.year,l.country from imdb,olympics-\
    ... locations where i.rating>'9.0',l.year>'1994',l.country='Canada'"
    >>> test = _parse_query(query)
    >>> test == {'from': ['locations'], 'where': ["i.rating>'9.0'",
    ... "l.year>'1994'", "l.country='Canada'"], 'select': ['i.rating',
    ... 'l.year', 'l.country']}
    True

    >>> query = "select o.year,l.year,o.sport from olympics-results,\
    ... olympics-locations where o.year>l.year,l.year='2002',o.\
    ... sport='Speed skating'"
    >>> test = _parse_query(query)
    >>> test == {'from': ['olympics-locations'], 'where': ["skating'"],
    ... 'select': ['o.year', 'l.year', 'o.sport']}
    True

    >>> query = "select i.rating,a.category from imdb,oscar-actor"
    >>> test = _parse_query(query)
    >>> test == {'from': ['imdb', 'oscar-actor'], 'where': None,
    ... 'select': ['i.rating', 'a.category']}
    True

    >>> query = (
    ... "select * from olympics-locations,olympics-results where " +
    ... "l.year=o.year")
    >>> test = _parse_query(query)
    >>> test == {'from': ['olympics-locations', 'olympics-results'],
    ... 'where': ['l.year=o.year'], 'select': ['*']}
    True
    '''
    # Holds all the keywords that will be present in the query
    KEYWORDS = {"select", "from", "where"}
    # Organizes specific tokens from the query to their respected keywords
    keyword_to_tokens = {"select": None,
                         "from": None,
                         "where": None}
    # Split the query into seperate elements
    query = query.split(maxsplit=5)
    # Go through each element in the query
    for element in query:
        # If the element is a keyword for the query
        if (element in KEYWORDS):
            # Set the key that will be accessed to the dictionary to said
            # element
            key = element
        # Else, the element must not be a keyword
        else:
            # Therefore, we split the element by the token ',' to get all the
            # important values
            element = element.split(',')
            # Then we add this element to the current key selected for
            # the dictionary
            keyword_to_tokens[key] = element
    # Returns the dictionary of organized keywords to tokens
    return keyword_to_tokens


# Private class
class _Keywords():
    '''Represents keyword constraints for a query.'''

    def __init__(self, keyword_to_tokens):
        '''(_Keywords, dict of {str: list of str}) -> NoneType
        Given a dictionary where the "keys" are keywords in the query, and
        the "values" are the tokens related to the query, keyword_to_tokens:
        Initilizes a _Keywords object that holds methods
        on how to process different word constraints.
        REQ: keyword_to_tokens restricted to the following format:
             |<keyword>: list of <tokens>|
             - keyword refers to elements in {"select", "from", "where"}
             - tokens refers to properly formatted commands based off what
               what keyword "key" they correspond to.
        '''
        # Initilize default variables for _Keywords object
        self._from_tokens = keyword_to_tokens["from"]
        self._where_tokens = keyword_to_tokens["where"]
        self._select_tokens = keyword_to_tokens["select"]

    def _get_select_tokens(self):
        '''(_Keywords) -> list of str
        Returns the list of tokens corresponding to the keyword "select".
        '''
        # Obtain the list of tokens
        select_tokens = self._select_tokens
        # Returns the "select" tokens
        return select_tokens

    def _get_from_tokens(self):
        '''(_Keywords) -> list of str
        Returns the list of tokens corresponding to the keyword "from".
        '''
        # Obtain the list of tokens
        from_tokens = self._from_tokens
        # Returns the "from" tokens
        return from_tokens

    def _get_where_tokens(self):
        '''(_Keywords) -> list of str
        Returns the list of tokens corresponding to the keyword "where".
        '''
        # Obtain the list of tokens
        where_tokens = self._where_tokens
        # Returns the "where" tokens
        return where_tokens

    def _process_where_tokens(self, table):
        '''(_Keywords, Table) -> Table
        Given a table object: Returns a new table that contains only the
        rows specified from the conditions in the where token constraints.
        REQ: table is non-empty
        '''
        # Obtain the where tokens to be processed
        where_tokens = self._get_where_tokens()
        # Create a new table
        proccessed_table = table.copy_table()
        # Go through each where token that needs to be processed
        for where_token in where_tokens:
            # If the token contains "=" and is a comparison between a hard
            # coded value
            if (('=' in where_token) and (where_token[-1][0] == "'")):
                # Split the token at the "="
                proccessed_where_token = where_token.split('=')
                # Proccess where token case 4
                proccessed_table = (
                    self._process_where_token_greater_than_case_4(
                      proccessed_where_token, proccessed_table))
            # If the token contains "=" and is not a comparison between a hard
            # coded value
            elif (('=' in where_token) and (where_token[-1][0] != "'")):
                # Split the token at the "="
                proccessed_where_token = where_token.split('=')
                # Proccess where token case 3
                proccessed_table = (
                    self._process_where_token_greater_than_case_3(
                     proccessed_where_token, proccessed_table))
            # If the token contains ">" and is a comparison between a hard
            # coded value
            elif (('>' in where_token) and (where_token[-1][0] == "'")):
                # Split the token at the ">"
                proccessed_where_token = where_token.split('>')
                # Proccess where token case 1
                proccessed_table = (
                    self._process_where_token_greater_than_case_1(
                     proccessed_where_token, proccessed_table))
            # If the token contains ">" and is not a comparison between a hard
            # coded value
            elif (('>' in where_token) and (where_token[-1][0] != "'")):
                # Split the token at the ">"
                proccessed_where_token = where_token.split('>')
                # Proccess where token case 2
                proccessed_table = (
                    self._process_where_token_greater_than_case_2(
                        proccessed_where_token, proccessed_table))
        # Returns the proccessed result of the where token
        return proccessed_table

    def _process_where_token_greater_than_case_1(self, where_tokens, table):
        '''(_Keywords, list of str, Table) -> Table
        Given a list of where_tokens; and a table object: Returns a new table
        containing only the rows that had a specific element in the row be
        greater in value than a hard coded value.
        REQ: table is non-empty
        '''
        # Create a copy of the table we are dealing with
        new_table = table.copy_table()
        # Seperate the where token elements
        main_column = where_tokens[0]
        hard_value = where_tokens[-1].strip("'")
        # Obtain the column data of the main column
        main_column_data_raw = new_table.get_column(main_column)
        # Place the raw elements of the main column into a list
        main_column_data = main_column_data_raw[main_column]
        # Obtain the number of rows of the table
        num_rows = new_table.num_rows()
        # Used to indicate which row to remove from the table
        removal_location = 0
        # Go through both column data elements at the same time
        for row in range(num_rows):
            # If the hard_value element is greater than the main column
            # element
            if (not(main_column_data[row] > hard_value)):
                # Update the table to reflect that this row failed the test
                new_table.remove_row(removal_location)
                # Then alter the removal location to factor in that the
                # table has one less row now
                removal_location -= 1
            # Increment the removal location
            removal_location += 1
        # Returns the table that passes the where token greater than case 1
        return new_table

    def _process_where_token_greater_than_case_2(self, where_tokens, table):
        '''(_Keywords, list of str, Table) -> Table
        Given a list of where_tokens; and a table object: Returns a new table
        containing only the rows that had a specific element in the row be
        greater in value than a specific element in another part of the row.
        REQ: table is non-empty
        '''
        # Create a copy of the table we are dealing with
        new_table = table.copy_table()
        # Seperate the where token elements
        main_column = where_tokens[0]
        secondary_column = where_tokens[-1]
        # Obtain the column data of the main column
        main_column_data_raw = new_table.get_column(main_column)
        # Obtain the column data of what the main column data will compare to:
        # the secondary column
        secondary_column_data_raw = new_table.get_column(secondary_column)
        # Place the raw elements of each column into individual lists
        main_column_data = main_column_data_raw[main_column]
        secondary_column_data = secondary_column_data_raw[secondary_column]
        # Obtain the number of rows of the table
        num_rows = new_table.num_rows()
        # Used to indicate which row to remove from the table
        removal_location = 0
        # Go through both column data elements at the same time
        for row in range(num_rows):
            # If the secondary column element is greater than the main column
            # element
            if (not(main_column_data[row] > secondary_column_data[row])):
                # Update the table to reflect that this row failed the test
                new_table.remove_row(removal_location)
                # Then alter the removal location to factor in that the
                # table has one less row now
                removal_location -= 1
            # Increment the removal location
            removal_location += 1
        # Returns the table that passes the where token greater than case 2
        return new_table

    def _process_where_token_greater_than_case_3(self, where_tokens, table):
        '''(_Keywords, list of str, Table) -> Table
        Given a list of where_tokens; and a table object: Returns a new table
        containing only the rows that had a specific element in the row be
        equal in value than a specific element in another part of the row.
        REQ: table is non-empty
        '''
        # Create a copy of the table we are dealing with
        new_table = table.copy_table()
        # Seperate the where token elements
        main_column = where_tokens[0]
        secondary_column = where_tokens[-1]
        # Obtain the column data of the main column
        main_column_data_raw = new_table.get_column(main_column)
        # Obtain the column data of what the main column data will compare to:
        # the secondary column
        secondary_column_data_raw = new_table.get_column(secondary_column)
        # Place the raw elements of each column into individual lists
        main_column_data = main_column_data_raw[main_column]
        secondary_column_data = secondary_column_data_raw[secondary_column]
        # Obtain the number of rows of the table
        num_rows = new_table.num_rows()
        # Used to indicate which row to remove from the table
        removal_location = 0
        # Go through both column data elements at the same time
        for row in range(num_rows):
            # If the main column element is not equal to the secondary column
            # element
            if (main_column_data[row] != secondary_column_data[row]):
                # Update the table to reflect that this row failed the test
                new_table.remove_row(removal_location)
                # Then alter the removal location to factor in that the
                # table has one less row now
                removal_location -= 1
            # Increment the removal location
            removal_location += 1
        # Returns the table that passes the where token greater than case 3
        return new_table

    def _process_where_token_greater_than_case_4(self, where_tokens, table):
        '''(_Keywords, list of str, Table) -> Table
        Given a list of where_tokens; and a table object: Returns a new table
        containing only the rows that had a specific element in the row be
        equal in value than a hard coded value.
        REQ: table is non-empty
        '''
        # Create a copy of the table we are dealing with
        new_table = table.copy_table()
        # Seperate the where token elements
        main_column = where_tokens[0]
        hard_value = where_tokens[-1].strip("'")
        # Obtain the column data of the main column
        main_column_data_raw = new_table.get_column(main_column)
        # Place the raw elements of the main column into a list
        main_column_data = main_column_data_raw[main_column]
        # Obtain the number of rows of the table
        num_rows = new_table.num_rows()
        # Used to indicate which row to remove from the table
        removal_location = 0
        # Go through both column data elements at the same time
        for row in range(num_rows):
            # If the main column element is not equal the hard value element
            # element
            if (main_column_data[row] != hard_value):
                # Update the table to reflect that this row failed the test
                new_table.remove_row(removal_location)
                # Then alter the removal location to factor in that the
                # table has one less row now
                removal_location -= 1
            # Increment the removal location
            removal_location += 1
        # Returns the table that passes the where token greater than case 4
        return new_table

    def _proccess_select_tokens(self, table):
        '''(_Keywords, Table) -> Table
        Given a table object: Returns a new table that contains only the
        column names specified from the select token constraints.
        REQ: table is non-empty
        '''
        # If the select token is "*", we get all the column datas from the
        # table
        get_all_column_data = "*"
        # Obtain the select tokens to be processed
        select_tokens = self._get_select_tokens()
        # Holds all column data that will be kept for the new table
        column_data = list()
        # Obtain all possible column names from the initial table
        column_names = table.get_column_names()
        # Check if we are actually getting all the column datas
        if (select_tokens[0] == get_all_column_data):
            # If so, place the neccessary column names required
            select_tokens = column_names
        # Go through each column name given by the select token
        for select_token in select_tokens:
            # Obtain the specified column name's data from the table
            raw_column_data = table.get_column(select_token)
            # Then add the column data to our selection of wanted columns
            column_data.append(raw_column_data)
        # Create a new table
        new_table = Table()
        # Go through each column data that will be kept for the new table
        for data in column_data:
            # Add the column data to our new table
            new_table.add_column(data)
        # Returns the final combination of column datas specified by the
        # "select" constraint
        return new_table

    def _process_from_tokens(self, database):
        '''(_Keywords, Database) -> Table
        Given a database: Returns a table object that is a combination of all
        the tables specified from the "from" token constraints.
        REQ: database is non-empty
        '''
        # Obtain the from tokens to be processed
        from_tokens = self._get_from_tokens()
        # Holds all tables that will be accessed from the database
        tables = list()
        # Go through each from token that needs to be processed
        for from_token in from_tokens:
            # Obtain the table from the database
            raw_table = database.get_table(from_token)
            # Then add it to our list of tables
            tables.append(raw_table)
        # Holds the initial table before performing Cartesian products
        initial_table = tables[0]
        # Delete that table from our list
        del tables[0]
        # Increments index-position values inside the loop
        index = 0
        # While there is an additional table ahead of the current table,
        # regarding our list of tables
        while (len(tables) > index):
            # Helper function: Perform a Cartesian product between the current
            # and following table
            cartesian_product_table = cartesian_product(
                initial_table, tables[index])
            # Sets the next table that will undergo the Cartesian product
            initial_table = cartesian_product_table
            # Increment by 1 through the list
            index += 1
        # Returns the final combination of tables specified by the "from"
        # constraint
        return initial_table


def run_query(database, query):
    '''(Database, str) -> Table
    Given a database, and a query: Returns the requested table from the
    database based on what was entered in the query.
    REQ: query restricted to the following format:
        |select <token> from <token> where <token>|
        - Where each additional token is seperated by ','
        - No spaces are allowed to be in the token, or beside the token
        - The keyword "where" is optional for the query
    REQ: query is non-empty
    >>> query = (
    ... "select * from seinfeld-foods,seinfeld-episodes where e.food=f.food")
    >>> database = read_database()
    >>> table = run_query(database, query)
    >>> result = table.get_dict()
    >>> result == {'e.season': ['0', '1', '1', '1', '1', '1', '1',
    ... '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '0',
    ... '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2',
    ... '2', '2', '2', '2', '2'], 'f.type': ['Condiments', 'Fruit', 'Junkfood',
    ... 'Meat', 'Rice/Pasta', 'Sandwiches', 'Sandwiches', 'Sandwiches',
    ... 'Sandwiches', 'Sandwiches', 'Soup', 'Bakery', 'Bakery', 'Condiments',
    ... 'Dairy', 'Dairy', 'Dip', 'Drinks', 'Drinks', 'Drinks', 'Drinks',
    ... 'Drinks', 'Drinks', 'Drinks', 'Fruit', 'Fruit', 'Junkfood', 'Junkfood',
    ... 'Junkfood', 'Junkfood', 'Meat', 'Meat', 'Meat', 'Seafood',
    ... 'Vegetables', 'Vegetables', 'Vegetables', 'Vegetables'],
    ... 'e.name': ['Good News Bad News', 'The Stock Tip', 'The Stake Out',
    ... 'Male Unbonding', 'Male Unbonding', 'The Robbery', 'The Robbery',
    ... 'The Stock Tip', 'Male Unbonding', 'Male Unbonding', 'The Stake Out',
    ... 'The Jacket', 'The Statue', 'The Busboy', 'The Chinese Restaurant',
    ... 'The Statue', 'The Stranded', 'The Baby Shower', 'The Jacket',
    ... 'Good News Bad News', 'The Phone Message', 'The Jacket', 'The Statue',
    ... 'The Jacket', 'The Phone Message', 'The Ex-Girlfriend', 'The Busboy',
    ... 'The Heart Attack', 'The Heart Attack', 'The Statue',
    ... 'The Chinese Restaurant', 'The Heart Attack', 'The Heart Attack',
    ... 'The Heart Attack', 'The Heart Attack', 'The Pony Remark',
    ... 'The Pony Remark', 'The Heart Attack'], 'f.food': ['Salad Dressing',
    ... 'Grape', 'Chocolate Covered Cherries', 'Meat Loaf', 'Pizza', 'BLT',
    ... 'Brisket Sandwich', 'Egg Salad', 'Egg Salad', 'Turkey Roll',
    ... 'Bouillabaisse', 'Mini Ritz', 'Pastries (of the Gods)', 'Pesto',
    ... 'Egg Rolls', 'French Toast', 'Good Dip', 'Bosco', 'Club Soda',
    ... 'Coffee', 'Coffee', 'Cranberry juice with two limes', 'Molotov Cocktail',
    ... 'Scotch', 'Apple', 'Cantaloupe', 'Cashews (bag of)',
    ... 'Chuckles (5 flavors)', 'Ice Cream', 'Ice Cream',
    ... 'Hamburger (Skyburger)', 'Salami', 'Bologna', 'Halibut', 'Cucumber',
    ... 'Foliage (edible)', 'Peas', 'Pickle'], 'e.food': ['Salad Dressing',
    ... 'Grape', 'Chocolate Covered Cherries', 'Meat Loaf', 'Pizza', 'BLT',
    ... 'Brisket Sandwich', 'Egg Salad', 'Egg Salad', 'Turkey Roll',
    ... 'Bouillabaisse', 'Mini Ritz', 'Pastries (of the Gods)', 'Pesto',
    ... 'Egg Rolls', 'French Toast', 'Good Dip', 'Bosco', 'Club Soda',
    ... 'Coffee', 'Coffee', 'Cranberry juice with two limes',
    ... 'Molotov Cocktail', 'Scotch', 'Apple', 'Cantaloupe',
    ... 'Cashews (bag of)', 'Chuckles (5 flavors)', 'Ice Cream',
    ... 'Ice Cream', 'Hamburger (Skyburger)', 'Salami', 'Bologna',
    ... 'Halibut', 'Cucumber', 'Foliage (edible)', 'Peas', 'Pickle']}
    True
    '''
    # Tells us that the where keyword does not need to be proccessed
    ignore_where_keyword = None
    # Proccess the query
    raw_query = _parse_query(query)
    # Create the table that will be returned
    requested_table = Table()
    # Create the object required to proccess keyword constraints found in the
    # entered query
    keyword_proccessing = _Keywords(raw_query)
    # Proccess the "from" keyword
    requested_table = keyword_proccessing._process_from_tokens(database)
    # Obtain the where token properties found in the given query
    where_tokens = keyword_proccessing._get_where_tokens()
    # If there are where tokens to be proccessed
    if (where_tokens != ignore_where_keyword):
        # Proccess the "where" keyword
        requested_table = (
        keyword_proccessing._process_where_tokens(requested_table))
    # Proccess the "select" keyword
    requested_table = (
        keyword_proccessing._proccess_select_tokens(requested_table))
    # Returns the table that was requested by the user
    return requested_table

if(__name__ == "__main__"):
    start_time = time.time()
    # Obtain the database in the file directory
    database = read_database()
    query = input("Enter a SQuEaL query, or a blank line to exit: ")
    # Keep proccessing queries until user enters a blank line
    while (query):
        # Obtain the requested table
        requested_table = run_query(database, query)
        # Output the requested table
        requested_table.print_csv()
        # Ask user for another query
        print (time.time() - start_time)
        a = time.time() - start_time
        query = input("Enter a SQuEaL query, or a blank line to exit: ")
