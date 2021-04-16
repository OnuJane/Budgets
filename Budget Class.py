budgetDict = [{
    'category:"food", "amount": 0,'
    },{
        "category: 'cloths', 'amount': 0,"
    },{
        "category: 'entertainment','amount': 0,"
    }]

class Budget:
    def __init__(self):
        pass

    def deposit(self):
        print('Budget Options')
        print('1. Food')
        print('2. cloth')
        print('3. entertainment')
        print('4. Exit')
        budgetselection = int(input('Please select your budget \n'))

        if budgetselection == 1:
            print('Food Balance: ', budgetDict[0]['amount'])
            question = int(input('What do you want to do? 1.deposit 2.Withdraw 3. Transfer 4. Exit \n'))
            if question == 1:
                deposit = int(input('Please enter amount: \n'))
                depositplus = budgetDict[0]['amount'] + deposit
                budgetDict[0]['amount'] = budgetDict[0]['amount'] + deposit
                print('New Balance: ', budgetDict[0]['amount'])
            elif question == 2:
                self.withdrawal()
            elif question == 3:
                self.Transfer()
            elif question == 4:
                exit()
            else:
                print('Do have a nice day, thank you')
            else print('Invalid selection, please check the options and try again')
            self.deposit()



        elif budgetselection == 2:
            print('Cloth Balance: ', budgetDict[0]['amount'])
            question = int(input('What do you want to do? 1.deposit 2.Withdraw 3. Transfer 4. Exit \n'))
            if question == 1:
                deposit = int(input('Please enter amount: \n'))
                depositplus = budgetDict[0]['amount'] + deposit
                budgetDict[0]['amount'] = budgetDict[0]['amount'] + deposit
                print('New Balance: ', budgetDict[0]['amount'])
            elif question == 2:
                self.withdrawal()
            elif question == 3:
                self.Transfer()
            elif question == 4:
                exit()
            else:
                print('Do have a nice day, thank you')
            else print('Invalid selection, please check the options and try again')
            self.deposit()

        elif budgetselection == 3:
            print('Entertainment Balance: ', budgetDict[0]['amount'])
            question = int(input('What do you want to do? 1.deposit 2.Withdraw 3. Transfer 4. Exit \n'))
            if question == 1:
                deposit = int(input('Please enter amount: \n'))
                depositplus = budgetDict[0]['amount'] + deposit
                budgetDict[0]['amount'] = budgetDict[0]['amount'] + deposit
                print('New Balance: ', budgetDict[0]['amount'])
            elif question == 2:
                self.withdrawal()
            elif question == 3:
                self.Transfer()
            elif question == 4:
                exit()
            else:
                print('Do have a nice day, thank you')
            else print('Invalid selection, please check the options and try again')
            self.deposit()
        elif budgetselection == 4:
            print ('Thank you')
            exit()


    def withdrawal(self):
        print(budgetDict)
        print('Where do you want to withdraw from?')
        print('1.Food')
        print('2.Cloth')
        print('3.entertainment')
        print ('4.exit')
        Option = int(input())

                
                 
