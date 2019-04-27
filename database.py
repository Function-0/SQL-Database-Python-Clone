# NOTE TO TA: DO NOT MIND THE LONG PROCCESSING TIMES. THIS PROGRAM MAY BE
# INEFFICIENT, BUT I ASSURE YOU THAT THIS PROGRAM WILL PROCESS THE REQUESTED
# QUERY... EVENTUALLY
# ==========================================================================
# Doctest examples for the following private helper function would be too
# convoluted to be of any benifit


def _update_table(self,
                  table_name=str(),
                  columns=list(),
                  rows=list(),
                  column_to_row=dict()):
    '''(Table[, str, list of str, list of [list of str],
    dict of {str: list of str}]) -> NoneType
    Updates the table when only changing specific properties of it.
    '''
    # Obtain all private variable values of table
    p_table_name = self.get_table_name()
    p_columns = self.get_column_names()
    p_rows = self.get_rows()
    p_column_to_row = self._column_to_row
    # Checks if the column_to_row has changed
    is_column_to_row_different = False
    # Check each options parameter to see if it has been altered or not
    # If the table name has changed
    if (table_name != str()):
        # Update table name value
        p_table_name = table_name
        # Then update the table's name
        self._table_name = p_table_name
    # If the columns have changed
    if (columns != list()):
        # Update table columns value
        p_columns = columns
    # If the rows have changed
    if (rows != list()):
        # Update table rows value
        p_rows = rows
    # If the column_to_row dict had changed
    if (column_to_row != dict()):
        # Update the column_to_row dict value
        p_column_to_row = column_to_row
        # Then notify the program of this change
        is_column_to_row_different = True
    # Update the table using the column_to_row dict value if it has changed
    if (is_column_to_row_different):
        _dict_set_up_table(self, p_column_to_row)
    # Else, update the table using the column names and rows data
    else:
        _list_set_up_table(self, (p_columns, p_rows))
    # Therefore, we cover all possible updates that the user could make


def _list_set_up_table(self, table_list_tuple):
    '''(Table, tuple of (list of str)) -> NoneType
    Given a table object, self; and a tuple of two lists, where the first list
    contains all the column names of the table, and the second list contains
    all the completed rows of the table, table_list_tuple: Sets up the private
    variables for the table object's table representation.
    REQ: table_list_tuple restricted to following format:
         |(list of column names, list of completed table rows)|
    '''
    # Set up table's column names
    self._columns = table_list_tuple[0]
    # Set up table's rows
    self._rows = table_list_tuple[-1]
    # Set up dict interpretation of table
    self._column_to_row = _list_to_dict_representation(table_list_tuple)


def _dict_set_up_table(self, dictionary):
    '''(Table, dict of {str: list of str}) -> NoneType
    Given a table object, self; and a dictionary where the keys are the column
    names of a table, and the values are the elements that are related to a
    specific column name, dictionary: Sets up the private variables for the
    table object's table representation.
    REQ: len(dictionary) > 0
    REQ: dictionary restricted to following format:
         |column name: elements related to column name|
    '''
    # Convert dictionary table representation into list table representation
    list_table_representation = _dict_to_list_representation(dictionary)
    # Sets up the private variables for the table object
    _list_set_up_table(self, list_table_representation)


def _list_to_dict_representation(table_list_tuple):
    '''(tuple of (list of str)[,list of int]) -> dict of {str: list of str}
    Given a tuple of two lists, where the first list contains all the column
    names of the table, and the second list contains all the completed rows
    of the table, table_list_tuple: Returns a dictionary where the keys are the
    column names of a table, and the values are the elements that are related
    to a specific column name.
    REQ: table_list_tuple restricted to following format:
         |(list of column names, list of completed table rows)|
    '''
    # Obtain the table's column names
    column_names = table_list_tuple[0]
    # Obtain the table's column rows
    rows = table_list_tuple[-1]
    # Holds the dictionary that we are creating
    column_to_elements = dict()
    # Add the table's columns to the dictionary
    for column_name in column_names:
        # Set up the list to hold the column's elements
        column_to_elements[column_name] = list()
    # Keep accessing the list until all columns are filled with their elements
    for index in range(len(column_names)):
        # Go through each completed row in the table
        for row in rows:
            # Add the specified row element to form part of the column's
            # elements
            column_to_elements[column_names[index]] += [row[index]]
    # Returns the dictionary of column names as keys, and column elements as
    # values
    return column_to_elements


def _dict_to_list_representation(dictionary):
    '''(dict of {str: list of str}[,list of int]) -> tuple of (list of str)
    Given a dictionary where the keys are the column names of a table, and the
    values are the elements that are related to a specific column name,
    dictionary: Returns a tuple of two lists, where the first list contains all
    the column names of the table, and the second list contains all the
    completed rows of the table.
    REQ: len(dictionary) > 0
    REQ: dictionary restricted to following format:
         |column name: elements related to column name|
    '''
    # Holds the table's column names/keys from the dictionary
    column_names = list(dictionary.keys())
    # Create a copy of the keys
    copy_column_names = column_names[:]
    # Obtain the the first column's value from the dictionary
    rows = dictionary[copy_column_names[0]]
    # Convert all of the elements in the first column into a list
    rows = [[item] for item in rows]
    # Delete the first column's key
    del copy_column_names[0]
    # Obtain the length of the first column's elements
    num_rows = len(rows)
    # Keep accessing the dictionary until all rows are created
    for turn in range(num_rows):
        # Go through each key in the dictionary to access their values
        # excluding the first column's key
        for column_name in copy_column_names:
            # Add the column's element to form parts of the row
            rows[turn].append(dictionary[column_name][turn])
    # Returns the tuple of list of column names and completed rows
    return (column_names, rows)
# Private helper functions end here
# =============================================================================


class Table():
    '''A class to represent a SQuEaL table'''

    def __init__(self):
        '''(Table) -> NoneType
        Initilizes a Table.
        '''
        # Initialize default variables for Table
        # Holds the name of the table for identification
        self._table_name = str()
        # Holds column names
        self._columns = list()
        # Holds full rows
        self._rows = list()
        # Holds: |key = column name; value = list of str that catogorize under
        # the column name|
        self._column_to_row = dict()

    def set_column_names(self, column_names):
        '''(Table, list of str) -> NoneType
        Given a sequence of column names for the table, column_names: Sets
        new column names to the Table.
        REQ: Each element in column_names holds one column name non-empty
        REQ: len(column_names) > 0
        '''
        # Set the column names for the table
        _update_table(self, columns=column_names)

    def set_table_name(self, table_name):
        '''(Table, str) -> NoneType
        Given a table_name: Sets the table's identification (name).
        REQ: len(table_name) > 0
        '''
        # Update the table's name
        _update_table(self, table_name=table_name)

    def get_table_name(self):
        '''(Table) -> str
        Returns the table identification (name). Default name is empty string.
        '''
        # Obtain the table's name
        table_name = self._table_name
        # Returns the name of the table
        return table_name

    def get_column(self, column_name):
        '''(Table, str) -> dict of {str: list of str}
        Given a column_name: Returns a dictionary where the key is the column
        name, and the values are the elements that are related to that
        specific column name.
        REQ: len(column_name) > 0
        REQ: column_name is present in table
        '''
        # Obtain the column of the table
        column_data = {column_name: self._column_to_row[column_name]}
        # Returns the column data specified
        return column_data

    def get_rows(self):
        '''(Table) -> list of [list of str]
        Return the rows available in the table.
        '''
        # Obtain the rows of the table
        rows = self._rows
        # Returns the table rows
        return rows

    def get_column_names(self):
        '''(Table) -> list of str
        Returns the column names available in the table.
        '''
        # Obtain the headers of the table
        column_names = self._columns
        # Returns the table headers
        return column_names

    def get_table_name(self):
        '''(Table) -> str
        Returns the table's identification (name).
        '''
        # Obtain the name of the table
        table_name = self._table_name
        # Returns the table name
        return table_name

    def num_rows(self):
        '''(Table) -> int
        Returns the number of rows in the table.
        '''
        # Obtain the rows of the table
        rows = self.get_rows()
        # Determine the number of rows in the table
        rows_num = len(rows)
        # Returns the amount of rows found in the table
        return rows_num

    def num_columns(self):
        '''(Table) -> int
        Returns the number of columns in the table.
        '''
        # Obtain the columns of the table
        columns = self.get_column_names()
        # Determine the number of columns in the table
        columns_num = len(columns)
        # Returns the amount of columns found in the table
        return columns_num

    def remove_column(self, column_name):
        '''(Table, str) -> NoneType
        Given a column_name: Removes the entire column from the table.
        REQ: column_name is present in table
        '''
        # Remove the column name from the table
        self._column_to_row.pop(column_name)
        # Obtain the remaining column names
        column_to_row = self._column_to_row
        # Update the table to reflect this change
        _update_table(self, column_to_row=column_to_row)

    def remove_row(self, row_number):
        '''(Table, int) -> NoneType
        Given a row_number: Removes said row from the table.
        The first row is considered the zeroth row of the table.
        REQ: removal_locations are vaild row numbers in table
        REQ: 0 <= row_number <= total amount of rows in the table
        '''
        # Delete the specified row from the table
        del self._rows[row_number]
        # Obtain the remaining rows
        rows = self.get_rows()
        # Update the table to reflect this change
        _update_table(self, rows=rows)

    def add_row(self, rows_info):
        '''(Table, list of str) -> NoneType
        Given a sequence of items in one row for the Table, rows_info:
        Adds the one row to the Table.
        REQ: len(rows_info) = number of columns in the table
        '''
        # Obtain the rows already in the table
        rows = self.get_rows()
        # Add the new rows to our list of rows for the table
        rows.append(rows_info)
        # Update the table to reflect this change
        _update_table(self, rows=rows)

    def add_column(self, column_info):
        '''(Table, dict of {str: list of str}) -> NoneType
        Given a dictionary where the keys are the column
        names of a table, and the values are the elements that are related to a
        specific column name, column_info:
        Adds all of the column data to the table.
        REQ: len(column_info value lists) = number of rows in the table
        REQ: len(column_info) = 1
        '''
        # Seperate the column data
        (column, row) = column_info.popitem()
        # Obtain the columns already in the table
        column_to_row = self._column_to_row
        # Add the new column to the ones already in the table
        column_to_row[column] = row
        # Update the table to reflect this change
        _update_table(self, column_to_row=column_to_row)

    def copy_table(self):
        '''(Table) -> Table
        Returns a copy of the table to prevent table mutation.
        '''
        # Create a new table
        copy_table = Table()
        # Obtain column names for the new table
        columns = self.get_column_names()
        # Obtain rows for the new table
        rows = self.get_rows()
        # Obtain table name for the new table
        table_name = self.get_table_name()
        # Update the copied table with this new information
        _update_table(copy_table,
                      table_name=table_name,
                      columns=columns,
                      rows=rows)
        # Returns the new copied table
        return copy_table

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_names: list_of_values
        '''
        # If the input is an empty dictionary
        if (new_dict == dict()):
            # Set up the private variables for the table object in a different
            # way
            _dict_set_up_table(self, {"": []})
            # self._column_to_row = new_dict
        # Sets up the private variables for the table object
        else:
            _dict_set_up_table(self, new_dict)

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        # Obtain the dictionary representation of the table
        dict_table_representation = self._column_to_row
        # Returns the dictionary representation of the table
        return dict_table_representation

    def print_csv(self):
        '''(Table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self.get_dict()
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))


class Database():
    '''A class to represent a SQuEaL database'''

    def __init__(self):
        '''(Database) -> NoneType
        Initilizes a Database.
        '''
        self._database_name = str()
        self._tables = list()
        self._name_to_table = dict()

    def add_table(self, table):
        '''(Database, Table) -> NoneType
        Given a table object: Adds the table to the database.
        REQ: table is non-empty
        '''
        # Store the table
        self._tables.append(table)
        # Store the table name as the key and the table itself as the value
        # for easy access to tables from the database based off of table names
        self._name_to_table[table.get_table_name()] = table

    def get_tables(self):
        '''(Database) -> list of Table
        Returns all the table objects found in the database.
        '''
        # Obtain the list of table objects
        tables = self._tables
        # Returns the tables found in the database
        return tables

    def get_table(self, table_name):
        '''(Database) -> Table
        Given a table_name: Returns the table that corresponds to said table
        name.
        REQ: len(table_name) > 0
        REQ: table_name is present in database
        '''
        # If the given table name is in the database
        if (table_name in self.get_table_names()):
            # Obtain the table from the database
            table = self._name_to_table[table_name]
            # Returns the specified table
            return table

    def get_table_names(self):
        '''(Database) -> list of str
        Returns a list of individual table identification (names) found in the
        database.
        '''
        # Obtain the tables in the database
        tables = self.get_tables()
        # Holds all the table names in the database
        table_names = list()
        # Go through each table in the database
        for table in tables:
            # Obtain the name of the table and add it to our list of table
            # names
            table_names.append(table.get_table_name())
        # Returns the list of table names
        return table_names

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        # Obtain the table name from the dictionary
        table_name = ' '.join(list(new_dict.keys()))
        # Place the table dictionary entry to the database
        self._name_to_table[table_name] = new_dict[table_name]

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        # Obtain the database keys along with database tables
        database_dict_representation = self._name_to_table
        # Returns the requested dictionary
        return database_dict_representation
