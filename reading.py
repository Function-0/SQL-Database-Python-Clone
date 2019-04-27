# NOTE TO TA: DO NOT MIND THE LONG PROCCESSING TIMES. THIS PROGRAM MAY BE
# INEFFICIENT, BUT I ASSURE YOU THAT THIS PROGRAM WILL PROCESS THE REQUESTED
# QUERY... EVENTUALLY
# ==========================================================================
# Functions for reading tables and databases

import glob
from database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
# file_list = glob.glob('csv_files/*.csv')  # Was originally glob.glob('*.csv')
# print(file_list)

# Write the read_table and read_database functions below

# Holds all possible escape character/blank space creators
ESCAPE_CHARACTERS = " \t\n\r\x0b\x0c"


def read_table(csv_file_name):
    '''(str) -> Table
    Given a csv_file_name: Returns a Table object that stores the csv file's
    coloumn and row information into a single unit.
    REQ: csv_file_name restricted to valid csv file names, and is non-empty
    '''
    # Open given csv file name
    csv_file_handle = open(csv_file_name, 'r')
    # Obtain all data from the file
    csv_data_copy = csv_file_handle.readlines()
    # Close the file
    csv_file_handle.close()
    # Create a Table object
    new_table = Table()
    # Remove trailing whitespace from sequence of column names
    formatted_column_names = str(csv_data_copy[0]).strip()
    # Convert the column names back into a list
    formatted_column_names = formatted_column_names.split(',')
    # Set the Table's column names
    new_table.set_column_names(formatted_column_names)
    # Remove trailing whitespace from sequence of rows
    # Go through each row in the data. We skip the first line of the file
    # b/c that line only contains the column names
    for row in csv_data_copy[1:]:
        # Strip the row into its individual elements
        elements_in_row = row.split(',')
        # Holds the formatted row
        new_row = str()
        # Stops creating a row for the table if invalid element is found in row
        is_invalid_row = False
        # Go through each element in the row
        for element in elements_in_row:
            # If the element does not contain any escape characters or is a
            # blank space
            if (element in ESCAPE_CHARACTERS):
                # This row is invalid
                is_invalid_row = True
            # If the element is valid for the row
            if ((element not in ESCAPE_CHARACTERS) and not (is_invalid_row)):
                # Remove trailing whitespace from the element
                new_element = element.strip()
                # Add the updated element to the formatted row
                new_row += ',' + new_element
        # If the element is valid for the row
        if ((element not in ESCAPE_CHARACTERS) and not (is_invalid_row)):
            # Convert the row back into a list
            formatted_row = new_row.split(',')[1:]
            # Add the formmatted row to the Table object
            new_table.add_row(formatted_row)
        # Reset invalid row detection
        is_invalid_row = False
    # Create the identification for the table
    new_table.set_table_name(csv_file_name[:csv_file_name.index('.')])
    # Returns the created Table
    return new_table


def read_database():
    '''() -> Database
    Accesses all csv files in the current directory: Then returns a Database
    object that stores each individual csv file's column and row information
    into a single unit.
    REQ: Table file(s) must be present in current directory for extraction
    '''
    # Create a Database object
    new_database = Database()
    # Obtain all file names in current directory
    file_names = glob.glob("*.csv")
    # Go through each file that needs to be accessed
    for file in file_names:
        # Helper function: Obtain the table related to the given csv file name
        new_table = read_table(file)
        # Add the table to the database
        new_database.add_table(new_table)
    # Returns the created database
    return new_database
