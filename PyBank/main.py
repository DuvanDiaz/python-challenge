import os
import csv

#path

data_budget = os.path.join("Resources", "budget_data.csv")

#read csv

P = []
Months = []

#determine change in revenue 
change_in_revenue = []

with open(data_budget, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    print(f"header: {csvheader}")

#loop through each row of data, skipping header
    for rows in csv_reader:
        P.append(int(rows[1]))
        Months.append(rows[0])
        


#loop / change in revenue , average revenue
 
    for x in range(1, len(P)):

        change_in_revenue.append((int(P[x]) - int(P[x-1])))

        avg_revenue = sum(change_in_revenue) / len(change_in_revenue)


#determine the time period (months)

T_Months = len(Months)

#greatest increase/decrease = PnL

max_profits = max(change_in_revenue)

max_losses = min(change_in_revenue)


#Print results

print("Financial Analysis")

print("----------------------------------------------------------")

print("Total Months: " + str(T_Months))

print("Total: " + str(sum(P)))

print("Average Change: " + "$" + str(avg_revenue))

print("Greatest Increase in Profits: " + str(Months[change_in_revenue.index(max(change_in_revenue))+1]) + " " + "$" + str(max_profits))

print("Greatest Decrease in Profits: " + str(Months[change_in_revenue.index(min(change_in_revenue))+1]) + " " + "$" + str(max_losses))


#Show results in a txt. file

file = open("analysis_results.txt","w")

file.write("Financial Analysis" + "\n")

file.write("-----------------------------------------------------------------------------------------------------------------")

file.write(" ")

file.write("Total Months: " + str(T_Months) + "\n")

file.write("Total: " + "$" + str(sum(P)) + "\n")

file.write("Average Change: " + "$" + str(avg_revenue) + "\n")

file.write("Greatest Increase in Profits: " + str(Months[change_in_revenue.index(max(change_in_revenue))+1]) + " " + "$" + str(max_profits) + "\n")

file.write("Greatest Decrease in Profits: " + str(Months[change_in_revenue.index(min(change_in_revenue))+1]) + " " + "$" + str(max_losses) + "\n")

file.close

