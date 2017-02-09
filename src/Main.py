accountList = {"zach": 343}

name = "zach2"
x = 500
accountList[name] = x


def login():
    global userName
    print("Welcome to The Bank of Python. Please enter your name.")
    userName = input()
    print("Hi ", userName, "!! How much would you like to deposit to start your account?", sep="")
    initDeposit = float(input())
    accountList[userName] = initDeposit


def menuSelect():
    print(
        "What would you like to do?:\n 1. Check Balance  2. Withdraw Funds  3. Deposit Funds"
        "  4. Cancel  5. DELETE ACCOUNT")
    optionSelect = input()

    if optionSelect == "1":
        print("Your current balance is", accountList[userName])
    elif optionSelect == "2":
        print("How much do you want to withdraw?")
        withdraw = float(input())
        accountList[userName] -= withdraw
    elif optionSelect == "3":
        print("How much would you like to deposit?")
        deposit = float(input())
        accountList[userName] += deposit
    elif optionSelect == "4":
        print("See you next time!")
    elif optionSelect == "5":
        print("Are you sure you want to DELETE your account? [yes] [no]")
        userInput = input()
        if userInput == "yes":
            del(accountList[userName])
        else:
            print("Okay, your account is not gone forever.")

        return


login()

menuSelect()








print("\n", accountList, "\n")
