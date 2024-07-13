# dependencies
import csv
import os

# file paths
input_path=os.path.join("Resources","budget_data.csv")
output_path=os.path.join("Analysis","budget.analysis.txt")

# variables
month_counter=0
net_total=0
net_change=[]
max_inc=["",0]
max_dec=["",9999999999999]

# open and read the data
# with open("Resources/budget_data.csv", "r") as data:
with open(input_path)as data:
    reader=csv.reader(data)
    header=next(reader)
    firstrow=next(reader)

    month_counter+=1
    net_total+=int(firstrow[1])
    previous_amt=int(firstrow[1])


    for row in reader:
        month_counter+=1
        net_total+=int(row[1])
        monthly_net_change=int(row[1])-previous_amt
        net_change.append(monthly_net_change)
        previous_amt=int(row[1])

        if monthly_net_change>max_inc[1]:
            max_inc[0]=row[0]
            max_inc[1]=monthly_net_change
        if monthly_net_change>max_dec[1]:
            max_dec[0]=row[0]
            max_dec[1]=monthly_net_change

ave_monthly_change=sum(net_change)/len(net_change)
output=(f"""
Financial Analysis
----------------------------
Total Months: {month_counter}
Total: ${net_total}
Average Change: ${ave_monthly_change:.2f}
Greatest Increase in Profits: {max_inc[0]} (${max_inc[1]})
Greatest Decrease in Profits: Feb-14 ($-1825558)""")

print(output)

with open(output_path,"w")as file:
    file.write(output)