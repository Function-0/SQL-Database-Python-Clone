# Holds file names for csv files
comma_seperated_values_file_names = (
    ["seinfeld-foods", 
     "seinfeld-episodes", 
     "oscar-film", 
     "oscar-actor", 
     "olympics-results", 
     "olympics-locations", 
     "imdb", 
     "boxoffice", 
     "books"])
 
# Open each csv file
for file_name in comma_seperated_values_file_names:
    file_handle = open(
        "/Users/Function/Desktop/Python Files/[CS] Assignment 2/csv_files/" + 
        file_name + ".csv", 'r')
    # Output file name
    print(file_name + ".csv")
    print("================================================================")
    # Output string data found in csv file
    # print(file_handle.read())
    file_handle.close()
    print("================================================================")
    file_handle = open(
        "/Users/Function/Desktop/Python Files/[CS] Assignment 2/csv_files/" + 
        file_name + ".csv", 'r')    
    file_data = file_handle.readlines()
    # Output list data (which contain escape characters) found in csv file
    for line in file_data:
        print([line])
    file_handle.close()
    print("================================================================")
    
    
