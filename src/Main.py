accountList = {"zach": 343}

name = "zach2"
x = 500
accountList[name] = x


def menuSelect(userInput):
    return {
        '1': print("Your current balance is", accountList[userName]),
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
    }


print("Welcome to The Bank of Python. Please enter your name.")

userName = input()

print("Hi ", userName, "!! How much would you like to deposit to start your account?", sep="")

initDeposit = input()

accountList[userName] = initDeposit
print(
    "What would you like to do?:\n 1. Check Balance  2. Withdraw Funds  3. Deposit Funds  4. Cancel  5. DELETE ACCOUNT")

optionSelect = input()

while optionSelect != '4':
    menuSelect(optionSelect)








# print("\n", accountList, "\n")
