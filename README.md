# election_analysis

## Project Overview
A Colorado Board of Elections employee needs to complete the election audit of a recent local congressional election, and get the following information:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software Python 3.9, Visual Studio Code 

## Election-Audit Results

The first thing we did in order to extract the information related to the elections results, we read a file directly from VS Code:

    with open(file_to_upload) as election_data:
        #read the file object with the reader function
        file_reader=csv.reader(election_data)

            #read the header row
        headers=next(file_reader)

            #print each row in the CSV file    
        for row in file_reader:

The analysis of the election shows that:

- There were *369,711 votes* cast in the election.

- The *County Votes* results were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)

And the code that was used to extract this results from the CSV file is the following:
    
        for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name=row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

- As noted in the caption below, *Denver*, was the county with the largest number of votes.
 
- The *Candidates* were:
  - Charles Casper
  - Diana DeGette
  - Raymon Anthony Doane
  
- The *Candidate Results* were:
  - Charles Casper Stockham: received 23.0% of the vote and 85,213 votes.
  - Diana DeGette: received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane: received 3.1% of the vote and 11,606 votes.
  
- The *Winner of the Election* was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

And finally to retreive the Candidates, the Candidate Results and the Winner of the Election we created the following script:

    #6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes=county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage=float(votes)/float(total_votes)*100

         # 6d: Print the county results to the terminal.
        county_vote=(

            f'{county_name}: {county_vote_percentage:.1f}% ({votes:,})\n')

        print(county_vote,end='')

         # 6e: Save the county votes to a text file.

        txt_file.write(county_vote)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes>winning_count_county):
            winning_count_county=votes
            winning_county=county_name
            
 Finally, we printed out the results into a text file:

<img width="286" alt="Screen Shot 2021-10-01 at 12 07 55" src="https://user-images.githubusercontent.com/78564912/135660438-7d55dbfd-3f2f-4799-8986-5074b90a89cf.png">

## Election-Audit Summary

To the Election Commission:

Given the versatility of the code we can add some features if we could have a richer CSV file in which we can:

1. Retrieve the total number and percentage of Democrat or Republican votes.
2. Comparative by county between Democrat and Republic votes.
