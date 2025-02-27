import random
import os
import time

#Variables for the menu options we will be using.
menu_options = {'D': 'Deposit', 'W': 'Withdraw', 'Q': 'Quit'}

#Initial Balance Starting for Customer
balance = random.uniform(-1000, 10000)

#Width and border setup for the ATM display
width = 40
border = '*' * width

#ATM Display Function
def atm_display(format_balance): #defining a function to display all the prompt of an ATM Display.
    print("")  #Blank line at the top
    print(border)#This will print * 40 times 
    print("PIXELL RIVER Financial".center(width))#Making sure to center PIXEL River by the border's width.
    print("ATM Simulator".center(width))  # Text centered below PIXELL RIVER FINANCIAL
    print(f"Your current balance is: {format_balance}".center(width))  # Formatted balance
    print("Deposit: D".center(width)) #Text centered above Your Current Balance Is:
    print("Withdraw: W".center(width))#Text centered above deposit
    print("Quit: Q".center(width))#Text centered above withdraw
    print(border)#print boarder

#Defining atm_simulator 
def atm_simulator():
    global balance  # without global this will be an error to the code. its to modify $$$
    user_input = '1000'#This ensures user input 
    
    #While user input does not equal to Q. 
    while user_input != 'Q':
        format_balance = f"${balance:,.2f}"  # Reformat balance to show as currency
        
        atm_display(format_balance)  # Display the ATM menu and balance
        response = 'Enter Your Selection: [D: Deposit, W: Withdraw, Q: Quit] '#The user User Interface for the program that tells the user "Enter Deposit, Withdraw and Quit".
        user_input = input(response).upper()  # To ensure user input is case-insensitive
        
        #Validate menu selection this ensures that the user is inputting the right Keywords examples D,W,Q. 
        if user_input not in menu_options:
            print(border)#This will print the border of * which prints 40 times 
            print("INVALID SELECTION".center(width))#If the user is inputting different letters it will print out Invalid Selection and Center the word along the width.
            print(border)#This will print the border of * and prints 40 times. 
            time.sleep(2)  # Wait for 2 seconds before continuing
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            continue  # Skip the rest of the loop and ask for input again

        #Deposit Option if user input equals to D then input transaction
        if user_input == 'D':
            deposit_input = input("Enter the transaction amount: $ ")#This ensures the user to input things on command prompt
            #Replace removes first decimal point from input, is digit only consists digit and input.count only one decimal point in original input.
            if deposit_input.replace('.', '', 1).isdigit() and deposit_input.count('.') <= 1:
                deposit_amount = float(deposit_input) 
                if deposit_amount > 0:
                    balance += deposit_amount  # Update the balance
                    print(f"You Deposited ${deposit_amount:,.2f}")
                else:
                    print("Deposit amount must be greater than zero.")
            else:
                print(border)
                print("INVALID SELECTION".center(width))
                print(border)

        #Withdraw Option else if user_input equals to W then enter transaction
        elif user_input == 'W':
            withdraw_input = input("Enter the transaction amount: $ ")
            #Replace removes first decimal point from input, is digit only consists digit and input.count only one decimal point in original input.
            if withdraw_input.replace('.', '', 1).isdigit() and withdraw_input.count('.') <= 1:
                withdraw_amount = float(withdraw_input)
                if withdraw_amount > 0 and withdraw_amount <= balance:#To Ensure users to not withdraw more than what is in the screen.
                    balance -= withdraw_amount  #Update the balance and modify it.
                    print(f"You Withdrew ${withdraw_amount:,.2f}.")
                elif withdraw_amount > balance: 
                    print(border)
                    print("INSUFFICIENT FUNDS".center(width))
                    print(border)
                else:
                    print("Withdrawal amount must be greater than zero.")
            else:
                print(border)
                print("INVALID SELECTION".center(width))
                print(border)

        #Quit Option elseif user_input equals Q then print (ATM Shutting Down), wait for prompt and clear the screen.
        elif user_input == 'Q':
            print("ATM Shutting Down")

        # Re-display the balance after each transaction
        time.sleep(2)  # Pause the script for 3 seconds
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

#Call the ATM simulator function to start the program
atm_simulator()