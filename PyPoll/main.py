def main():
    file = open(r"C:\Users\DuvanFelipe\Desktop\DataAnalysis_Coding_Assignments\python-challenge\PyPoll\Resources\election_data.csv")

    #set up dictionary for candidate names and # of votes

    Votes_candidates = dict()

    #set up total # of votes to 0

    Total_votes = (int(0))

    #loop through each row / list of tokens, 3 values in list

    for line in file:
        fields = line.strip().split(",")
        if len(fields) == 3:

        #fetching last value as name, if name not on candidates, add to it with value = 1

            name = fields[-1]
        if name not in Votes_candidates:
            Votes_candidates[name] = 1
        else:
            Votes_candidates[name] +=1

        #increment total # of votes 
        Total_votes +=1

    file.close()

    #Set winner to none / set dict. for candidate names and percentages

    Winner_Candidate = None
    Percentages = dict()

    #loop for candidates votes

    for candidate in Votes_candidates:
        Percentages[candidate] = (Votes_candidates[candidate] / Total_votes) * 100

        #setting up winner

        if Winner_Candidate == None or Votes_candidates[candidate] > Votes_candidates[Winner_Candidate]:
            Winner_Candidate = candidate

    #list for # of votes per candidate (dict keys), sorted by descending amount

    keys_sorted = sorted(Votes_candidates.keys(), key=lambda k: Votes_candidates[k], reverse=True)

    #print results

    print("Election Results")
    print("_" * 25)
    print("Total Votes: ", Total_votes)
    print("_" * 25)
    for candidate in keys_sorted:
         print("{}:{:.3f}% ({})".format(candidate, Percentages[candidate], Votes_candidates[candidate]))
    print("_" * 25)
    print("Winner: ", Winner_Candidate)
    print("_" * 25)

    #printing results in txt. file

    outfile = open("poll_results.txt", "w")
    print("Election Results", file=outfile)
    print("_" * 25, file=outfile)
    print("Total Votes: ", Total_votes, file=outfile)
    print("_" * 25, file=outfile)
    for candidate in keys_sorted:
         print("{}:{:.3f}% ({})".format(candidate, Percentages[candidate], Votes_candidates[candidate]), file=outfile)
    print("_" * 25, file=outfile)
    print("Winner: ", Winner_Candidate, file=outfile)
    print("_" * 25, file=outfile)
    outfile.close()

#close main
main()








