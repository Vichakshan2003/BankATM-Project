import datetime

information = {"Vick": ["Vickmaturu123", "password1234542"]}
bankBalances = {"Vick": "0"}
transactions = {"Vick": ["Account created on Tue Jul 21 9:00:00 2020", "Deposited 0 dollars on Tue Jul 21 9:00:00 2020"]}
y = 0
while y == 0:
    i = 0
    j = 0
    k = 0
    x = 0
    l = 0
    while i ==0:
        input1 = input("Thank you for choosing Chase. Select one of the following options: (Sign Up / Log In)")
        if input1.lower() == "sign up":
            var = str(CurrentName) in information
            while var:
                print("Name already exists.")
                CurrentName = input("What is your name? ")
                var = str(CurrentName) in information
            newUser2 = input("Please enter a Username:  ")
            newUser3 = input("Please enter a Password:  ")
            information[str(CurrentName)] = [str(newUser2), str(newUser2)]
            bankBalances[str(CurrentName)] = "0"
            currentTime = datetime.datetime.now()
            currentTransaction = "Account Created on " +currentTime.strftime("%c")
            transactions[str(CurrentName)] = [str(currentTransaction)]
            i =0
        elif input1.lower() == "log in":
            while x == 0:
                CurrentName = input("Enter you name:   ")
                var = str(CurrentName) not in information
                while var:
                    print("Name not found.")
                    CurrentName = input("Enter your name:  ")
                    var = str(CurrentName) not in information
                security1 = input("Enter your Username:  ")
                security2 = input("Enter your Password:  ")
                security3 = "['"+str(security1)+"', '"+str(security2)+"']"
                if str(security3) == str(information[CurrentName]):
                    x = 1
                    i = 1
                else:
                    print("Sorry! Incorrect Name / Username / Password")
        elif input1.lower() == "terminate":
            terminate = input("Enter password to terminate proccess:  ")
            if terminate == "t3rm1n4t3":
                i = 1
                j = 1
                k = 1
                x = 1
                y = 1
        else:
            print("Sorry! Something when wrong with your response.")
    while j == 0:
        transactionList = transactions.get(CurrentName)
        input2 = input("Would you like to: (Deposit / Withdraw/ Print History / Log Out ")
        k = 0
        if input2.lower() == "deposit":
            depositAmount = input("How much would you like to deposit?")
            while l ==1:
                l = 1
                try:
                    bankBalances[str(CurrentName)] = int(bankBalances[str(CurrentName)]) + int(depositAmount)
                    currentTime = datetime.datetime.now()
                    currentTransaction = "Deposited "+str(depositAmount)+" dollars on "+currentTime.strftime("%c")
                    transactionList.append(str(currentTransaction))
                    break
                except ValueError:
                    print("Invalid Input. Please try again.")
                    l = 0
            bankBalances[str(CurrentName)] = int(bankBalances[str(CurrentName)]) + int(depositAmount)
            print("Final Balance: "+str(bankBalances[str(CurrentName)]))
        elif input2.lower() == "withdraw":
            withdrawAmount = input("How much would you like to withdraw? ")
            while l == 1:
                l =1
                try:
                    bankBalances[str(CurrentName)] = int(bankBalances[str(CurrentName)]) + int(withdrawAmount)
                    currentTime = datetime.datetime.now()
                    currentTransaction = "Withdrawn " + str(depositAmount) + " dollars on " + currentTime.strftime("%c")
                    transactionList.append(str(currentTransaction))
                    break
                except ValueError:
                    print("Invalid Input. Please try again. ")
                    l = 0
            bankBalances[str(CurrentName)] = int(bankBalances[str(CurrentName)]) - int(withdrawAmount)
            print("Final Balance: " + str(bankBalances[str(CurrentName)]))
        elif input2.lower() == "print history":
            print("Transaction History:")
            for i in range(len(transactionList)):
                print((transactionList(i)))
        elif input2.lower() == "log out":
            j = 1
            transactions[CurrentName] = transactionList
        elif input2.lower() == "delete account":
            while k == 0:
                areYouSure = input("Are you sure you want to delete your account? (Yes/No ")
                if areYouSure.lower() == "yes":
                    del information[CurrentName]
                    del bankBalances[CurrentName]
                    del transactions[CurrentName]
                    j = 1
                    k = 1
                elif areYouSure.lower() == "no":
                    k =1
                else:
                    print("Invalid Input. ")
        else:
            print("Sorry! Something went wrong with your response")
        print("Process Terminated. All user (except for the default one) hae been erased.")






