import pprint
import csv

#Define in empty dictionary to store account balances
account_balances = {}

#Open the input file using a context manager
with open('account_balances.txt', 'r') as file:
    for line in file:
        #Split each line by the pipe delimiter
        account_number, balance = line.strip().split('|')
        
        #Add the account number and balance to the dictionary as float "converts to string to a number"
        account_balances[account_number] = float(balance)

#Pretty print the dictionary and show data before interest update
print("Account,Balances")

#formats the data and make easier to see structures of directories.
pprint.pprint(account_balances)

#Gather accounts and calculate interest
for account_number, balance in account_balances.items():
    if balance < 0:
        #Negative balances receive 10% interest charged
        interest_rate = 0.10
    elif balance < 1000:
        #Positive balances less than $1000 receive 1% interest
        interest_rate = 0.01
    elif balance < 5000:
        #Positive balances between $1000 and $5000 receive 2.5% interest
        interest_rate = 0.025
    else:
        #Positive balances $5000 and above receive 5% interest
        interest_rate = 0.05
    
    #Calculate interest based on balance and interest combined.
    interest = balance * interest_rate
    new_balance = balance + interest
    
    #Update the dictionary on the new balance
    account_balances[account_number] = new_balance

#Pretty print the updated account balances after interest has been applied
print("\nAccount Balances After Interest Update:")
pprint.pprint(account_balances)

#Save the updated account balances to a CSV file
filename = 'updated_balances_IE.csv'  

#Write the updated balances to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Account', 'Balance'])  #Write the header
    for account_number, balance in account_balances.items():
        writer.writerow([account_number, balance])


#Print and confirm that balances have been updated to CSV File 
print(f"\nAccount,Balance")