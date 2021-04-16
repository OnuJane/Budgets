 #creating bank operations

import random
import database
import visualization 
from getpass import getpass

database = {}    #dictionary 

def init():
    isvalidOptionSelected = False

    print('Welcome to Zeal Bank')
    while isvalidOptionSelected == False:

        Question = int(input('Do you have an account with us?: 1 (yes) 2 (No) \n'))
        if Question == 1:
            isvalidOptionSelected = True 
            login()
        elif Question == 2:
            isvalidOptionSelected = True
            print(register()) 
        else:
            print('Wrong Entry, input a valid option' )


def login(): 
    print('This is the login page')
    useraccountnumber = input('Please enter your account number: \n')
    isaccountnumbervalid = validation.account_number_validation(useraccountnumber)
    if isaccountnumbervalid:
        password = getpass('Please enter your password \n')
        user = database.authenticated_user(useraccountnumber.password)
        if user:

            BankOperations()
        else: 
            print('Invalid username or password, please try again')
            login()
    else:
        print('Invalid account number')
        init()

    


    

def register():
    email = input('Type in your email address: \n')
    first_name = input('Type in your first name: \n')
    last_name = input('Type in your last name: \n')
    password = input('create a unique password: \n')
    confirmpassword = input('Confirm the password you entered: \n')
    if password == confirmpassword:
        print('Password Confirmed')


    accountnumber = Generateaccountnumber()
    database[accountnumber]  = [first_name, last_name, email, password]
    isusercreated = database.create(accountnumber, first_name, last_name, email, password)
    if isusercreated:

        print("Account creation was successful")
        print('Your account number is: %d' % accountnumber)

        login()

def BankOperations(user):
    print('Welcome, %s %s' % (user[0], user[1]))
    selectedOption = int(input('Please select an option:1.deposit 2. withdrawal 3.Complain 4. Logout \n')) 

        Balance = 1200
        Deposit = []
        withdraw = []
    

        if (selectedOption == 1):
            print('You selected', selectedOption)
            deposit = int(input('How much do you want to deposit:\n'))
            print('Amount deposited successfully')
            Deposit.append(deposit)
            currentbalance = int(Balance + deposit)
            print(currentbalance)
            
        
        elif (selectedOption == 2):
            print('You selected', selectedOption)
            withdrawe = int(input('How much do you want to withdraw: \n'))
            print('Take your cash')
            withdraw.append(withdrawe)
            # if withdraw > Balance:
            print('Sorry, insufficient balance')

        elif (selectedOption == 3):
            print('You selected', selectedOption)
            Prompt = input('Please state your issue: \n')
            print('Thank you for contacting us')


        elif (selectedOption == 4):
            print('Thank you for banking with us')

        else: 
             print('Invalid Option, Check your input')   
             BankOperations(user)



def Generateaccountnumber(): 
    print('Generating Account number')
    return random.randrange(1111111111,9999999999)

    print(Generateaccountnumber())
    login()

##System intialization
init()