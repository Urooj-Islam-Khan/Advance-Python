print("Welcome to ATM Syystem")
username = input("Enter Username: ")
password = input("Enter Password: ")
print("\nLogin Successfully\n")

cuurentBalance = 1000
history = ["\n------------------Transaction Historyn------------------ \n"]

while True:
    
    print("1: Check Balance")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("4: View Transaction History")
    print("5: Exit")
    option = int(input("Enter an option: "))
    if option == 1:
        print("Your current balance is: $",cuurentBalance)
    elif option == 2:
        deposit = int(input("Enter amount to deposit:"))
        if deposit > 0:
            cuurentBalance += deposit
            history.append(f"Deposited: ${deposit}")
            print("Deposit Successful! New Balance: $",cuurentBalance)
        else:
            print("Invalid amount!")
    elif option == 3:
        withdraw = int(input("Enter amount to deposit:"))
        if 0 < withdraw:
            cuurentBalance -= withdraw
            history.append(f"Withdraw: ${withdraw}")
            print("Withdrawal Successful! New Balance: $", cuurentBalance)
    elif option == 4:
        print("\n".join(history))
        print("------------------------------------")
        print("Current Balance: $",cuurentBalance)
        print("------------------------------------\n")
    elif option == 5:
        print("Existing program. Thank you!")
        break
    else:
        print("Invalid option!")