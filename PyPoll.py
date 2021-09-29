# import datetime as dt

# now = dt.datetime.now()

# print('The time right now is:',now)

# #openfile direct path
# file_to_load='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_results.csv'

# election_data=open(file_to_load,'r')

# #perform analysis

# election_data.close()

# #openfile indirect path

# import os
# file_to_load=os.path.join('/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_results.csv')
# with open(file_to_load) as election_data:

#     #perform analysis

#     print(election_data)


# fileName='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_analysis.txt'

# outFile=open(fileName,'w')

# #write some data
# outFile.write('Hello world!')

# outFile.close()

# with open(fileName,'w') as txt_file:
#     txt_file.write('Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson')

import csv

# Assign a variable to load a file from a path.
file_to_load='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_results.csv'
file_to_save='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_analysis.txt'

#open file 
with open(file_to_load,'r') as election_data:
    #read the file object with the reader function.
    file_reader=csv.reader(election_data)

    #print each row in the CSV file
    # for row in file_reader:
    #     print(row)
    headers=next(file_reader)
    print(headers)

