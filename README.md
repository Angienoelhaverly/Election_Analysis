# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Calculate the amount of votes and percentage per county. 
6. Calculate the counties with the largest county voter turnouts. 
7. Determine the winner of the election based on popular vote. 

## Resources 
- Data Source: election_results.csv
- Software: Python 3.6.1 Visual Studio Code 1.38.1

## Election Audit Results
The analysis of the election show that: 
- There were 369,711 votes cast in the election. 
- The counties counted in the election were: 
    - Jefferson County
    - Denver County
    - Arapahoe County
- The county results were: 
    - Jefferson county received 10.5% of the total votes casted at 38,855 votes cast. 
    - Denver county received 82.8% of the total votes casted at 306,055 votes cast.
    - Arapahoe county received 6.7% of the total votes casted at 24,801 votes cast. 
- The county with the largest voter turnout was: 
    - Denver county with 306,055 votes cast, garnering 82.8% of the total votes cast in the whole election. 
- The candidates were: 
    - Charles Gasper Stockham 
    - Diana DeGette 
    - Raymon Anthony Doane 
- The candidates results were: 
    - Charles Gasper Stockham received 23% of the vote and 85,213 number of votes. 
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes. 
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes. 
- The winner of the election was: 
    - Diana DeGette who received 73.8% of the vote and 272,892 number of total votes. 

## Election Audit Summary
Dear Election Audit Commission, the script that was written for this election audit project is a valuable tool that can be used for many types of future election counting and auditing needs. The script first takes in a csv file that has 3 different columns (Ballot ID, County, and Candidate Voted for), reads the csv file, and analyzes the dataset. It then outputs the analyzed data into a text file for better visualization. The programs defines candidate options (Charles, Diana, or Raymon) as a list, and then creates a dictionary where it stores the candidate name as a key and how many votes the candidate receives as a value. It uses this same coding format for counting the votes per county to find the county with the largest voter turnout. Using repeition and decision statements, the script searches for how many candidates received how many votes, percentages, and calculates who won, all while printing out these results to a text file. 

This is a very general and useful script that could therefore be used as a template in the future for any future election such as a presidential election. If the script was a presidental election instead of a state congressional election, there would need to be a few more datasets analyzed. For example, the data would likely include data for states as well as counties and so there would be a whole other column for states. Election results would need to be broken down further by including the state and county election results. A nested loop with a decision statement where the county occurs inside the state would likely solve this. For example, the loop would need to run through all the counties in one state before it could move on to the next counties in the following state. Once it reached the end of the state rows, it could move on to the counties in the next state. A presidential election analysis might also require dataset for electoral college. For example, once a county received so many popular votes, the county would then automatically need to be assigned the electoral college votes. Then the same would go for the state electoral college. This could be accomplished with a few if statements. For example, if a county received a certain threshold of votes, then a dataset for a number of electoral college votes would automatically be assigned to the candidate. And the same for on the state level. 

Another application for this election analysis script could simply be a further in depth analysis of voting data gathered. For example, if you wanted to run an analysis based on demographics and how many votes each candidate received based on party lines (democrat, republican) or demographic data (such as race, sex, or age), you could easily add these as new columns to the dataset and apply the same decisison and repitition statements that were used for counting and assigning the total winning votes per candidate and per county. This would simply require a for loop counting votes per that demographic or party affiliation, getting the affiliation or demographic name, calculating the percentage, and then printing those results to the text file. Then an if statement would be used to determine the final counts per each segment and then print those total values to the results file. As you can see, there are many reasons why this script is a great beginning template to an election audit/analysis and there are many ways to further enhance the scope of the audit in any election. 
