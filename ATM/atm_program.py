import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Insert Yout Pin : "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Wrong Pin, Try Again: "))
        trial += 1
        if trial == 3:
            print("Error, Please take your card and try again.")
            exit()
        
    while True:
        print("Welcome to ATM")
        print(" 1 - Check Balance \n 2 - Debet \n 3 - Save \n 4 - Change PIN \n 5 - Exit")
        selectMenu = int(input("\nChoose what do you want ? \n"))

        if selectMenu == 1:
            print("Your Balance : ", str(atm.checkBalance()))
            chooseMenu = input("Do you want to continue or exit(y/n) : ")
            if chooseMenu == "y":
                pass
            else:
                exit()
            
        elif selectMenu == 2:
            nominal = float(input("Insert Your Withdrawn : "))
            verify_wd = input("Confirm: Here is your nominal withdraw(y/n) : " + str(nominal) + "\n=>")

            if verify_wd == "y":
                print("Your first balance is : ", str(atm.checkBalance()))
            else:
                break

            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Withdraw transaction successful")
                print("Your new balance is : "+ str(atm.checkBalance()))
            else:
                print("Sorry, your balance is not enough to withdraw\nPlease add your balance")

            chooseMenu = input("Do you want to continue or exit(y/n) : ")
            if chooseMenu == "y":
                pass
            else:
                exit()
        elif selectMenu == 3:
            nominal = float(input("Insert Your Deposit : "))
            verify_depo = input("Confirm: Here is your nominal deposit(y/n) : " + str(nominal) + "\n=>")

            if verify_depo == "y":
                atm.depositBalance(nominal)
                print("Your current balance is : " + str(atm.checkBalance()))
            else:
                break
            chooseMenu = input("Do you want to continue or exit(y/n) : ")
            if chooseMenu == "y":
                pass
            else:
                exit()
        elif selectMenu == 4:
            verifyPin = int(input("Insert your PIN : "))

            while verifyPin != int(atm.checkPin()):
                print("Wrong PIN, Please try again")

            updatedPin = int(input("Please input your ne PIN : "))
            print("Your PIN has been change")

            verify_newPin = int(input("Please insert your new PIN again : "))

            if verify_newPin == updatedPin:
                print("Successful")
            else:
                print("Wrong")
        elif selectMenu == 5:
            print("Receipt will print automatically while you exit\n Please keep it as proof of transaction")
            print("No. receipt\t: ", random.randint(10000, 1000000))
            print("Date \t\t: ", datetime.datetime.now())
            print("Last balance \t: ", atm.checkBalance())
            print("Thank you for using this ATM")
            exit()
        else:
            print("Something wrong, please try again..")
