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

# import csv

# # Assign a variable to load a file from a path.
# file_to_load='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_results.csv'
# file_to_save='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_analysis.txt'

# #open file 
# with open(file_to_load,'r') as election_data:
#     #read the file object with the reader function.
#     file_reader=csv.reader(election_data)

#     #print each row in the CSV file
#     # for row in file_reader:
#     #     print(row)
#     headers=next(file_reader)
#     print(headers)

import csv

file_to_upload='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_results.csv'
file_to_save='/Users/humbertorodriguez/Documents/Bootcamp_Data_Analyst/Module_3/Async/election_analysis/Resources/election_analysis.txt'

total_votes=0

candidate_options=[]

candidate_votes={}

winning_candidate=''

winning_count=0

winning_percentage=0

#open file
with open(file_to_upload) as election_data:

    #read the file object with the reader function
    file_reader=csv.reader(election_data)

        #read the headr row
    headers=next(file_reader)

        #print each row in the CSV file    
    for row in file_reader:

        #count each vote
        total_votes=total_votes+1

        #search for each candidate's name
        candidate_name=row[2]

        #if the candidate_name is not is candidate_options
        if candidate_name not in candidate_options:

            #add it to candidate options
            candidate_options.append(candidate_name)

            #adding candidate and tracking candidate's vote count in zero
            candidate_votes[candidate_name]=0

        #add 1 vote per loop to candidate_votes
        candidate_votes[candidate_name]+=1

with open(file_to_save,'w') as txt_file:
    elections_results=(
        f'Elections Results\n'
        f'------------------------------\n'
        f'Total Votes {total_votes:,}\n'
        f'------------------------------\n')

    print(elections_results)

    txt_file.write(elections_results)

    #for each candidate in the rows that is in candidate_votes
    for candidate_name in candidate_votes:
        #Access candidate_votes and retrieve vote count by candidate
        votes=candidate_votes[candidate_name]

        #Calculate % of votes
        vote_percentage=float(votes)/float(total_votes)*100

        candidate_results=(f'{candidate_name}: {vote_percentage:.1f}% {votes:,}\n')

        print(candidate_results)

        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        #for each loop if votes is greater than winnin_count and vote_% is greater
        #than winning_%...
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            #If true then set winning_count = votes and winning_percent =
            #vote_percentage.
            winning_count=votes
            winning_percentage=vote_percentage
            #also for this loop add the candidate_name to winning candidate
            winning_candidate=candidate_name

    winning_candidate_summary=(
        f'----------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Counting Vote: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-----------------------\n')

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
