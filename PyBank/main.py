
import os
import csv

# Set path for file
csvpath = os.path.join("Resources" , "budget_data.csv") 

# Create lists to store data
month = []
profit_loss = []
NewPL = []
OldPL = []
amount_change = []
month_adjusted = []




# Open the CSV
with open(csvpath, newline="") as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 

    # Loop through records
    for row in csvreader:
        month.append(row[0])  # now i have a list off the months 
        profit_loss.append(int(row[1])) # now i have a list for the P/L


total_amount = sum(profit_loss) # now i have a sum of All P/L
NewPL = profit_loss[1:]  # first number of P/L
OldPL = profit_loss[:-1] # last number of P/L

    
#     #  to find Average Change using lists:
amount_change = [new - old for (new, old) in zip(NewPL, OldPL)]  
#     #amount_change_test = profit_loss_table[]
avg_change = round((sum(amount_change) / len(amount_change)),2) # we are taking the avg + rounding to 2 dec point 

print(amount_change)
## Greatest Profit and Loss Values
# adjust month list to fit the amount_change list. It takes out the first value 
# since the first month does not have a change.
month_adjusted = month[1:]
# find the index number of the highest profit and loss amount in amount_change list
MaxIndex = amount_change.index(max(amount_change))
MinIndex = amount_change.index(min(amount_change))
MaxProfitMonth = month_adjusted[MaxIndex]
MinProfitMonth = month_adjusted[MinIndex]
MaxProfit = amount_change[MaxIndex]
MinProfit = amount_change[MinIndex]

# print final hw
print("----------------------------")
print("Finacial Analysis")
print("----------------------------")
print("Total Months: " + str(len(month)))
print("Total: " + "$" + format(total_amount, ","))
print("Average Change: " + "$" + format(avg_change,',.2f'))
print("Greatest Increase in Profits: " + MaxProfitMonth + " ($" + format(MaxProfit,',.2f') + ")")
print("Greatest Decrease in Profits: " + MinProfitMonth + " ($" + format(MinProfit, ',.2f') + ")")
print("----------------------------")

file = "PyBank_Report.txt"
with open(file,'w') as f:
    print("----------------------------",file=f)
    print("Finacial Analysis",file=f)
    print("----------------------------",file=f)
    print("Total Months: " + str(len(month)),file=f)
    print("Total: " + "$" + format(total_amount, ","),file=f)
    print("Average Change: " + "$" + format(avg_change,',.2f'),file=f)
    print("Greatest Increase in Profits: " + MaxProfitMonth + " ($" + format(MaxProfit,',.2f') + ")",file=f)
    print("Greatest Decrease in Profits: " + MinProfitMonth + " ($" + format(MinProfit, ',.2f') + ")",file=f)
    print("----------------------------",file=f)
    f.close()





# import pathlib
# import csv
# # create the path for the file 
# csvpath = pathlib.Path('Resources', 'budget_data.csv')

# # # open the file 
# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",") ## why ? 
#     cdv_header = next(csvreader)
#     rows = [i for i in csvreader]
# # Your task is to create a Python script that analyzes the records to calculate each of the following:
# # The total number of months included in the dataset
#     months = len(rows)
#     print(months)
# # The net total amount of "Profit/Losses" over the entire period

# profit= [1,2,3,]
# months = ['a','b', 'c' ]


# # # The average of the changes in "Profit/Losses" over the entire period

# # # The greatest increase in profits (date and amount) over the entire period

# # # The greatest decrease in losses (date and amount) over the entire period   