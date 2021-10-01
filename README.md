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

## Summary

The first thing we did in order to extract the information related to the elections results, we read a file directly from VS Code:

```with open(file_to_upload) as election_data:

    #read the file object with the reader function
    file_reader=csv.reader(election_data)

        #read the headr row
    headers=next(file_reader)

        #print each row in the CSV file    
    for row in file_reader:```

The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper
  - Diana DeGette:
  - Raymon Anthony Doane

In order to get the total vot cast we first defined a 

- The candidate results were:
  - Charles Casper Stockham: received 23.0% of the vote and 85,213 votes.
  - Diana DeGette: received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane: received 3.1% of the vote and 11,606 votes.
- The winner of the lection was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
