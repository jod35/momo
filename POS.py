def Momo():
    min_balance=2000
    deposit = 0
    new_balance= min_balance + deposit

    proceed=int(input("enter 0 to quit or any other number to continue "))
    while proceed !=0:
        print("\nwelcome to MTN Mobile Money!!\n1.Deposit money\n2.Check Balance\n3.Withdraw money\n0.Exit")
        reply=int(input("reply: "))
        if reply ==1:
            deposit= int(input("enter your deposit in UGX: "))
            if (deposit < 1000):
                print("you should deposit an amount greater than UGX 1000. ")
            else:
                new_balance = min_balance + deposit
                print("You have deposited UGX %d and your current balance is UGX %d. "%(deposit,new_balance))
        elif reply==2:
            print("Your current balance is UGX %d."%(new_balance))

        elif reply==3:
            withdraw=int(input("enter the amount you want to withdraw: "))
            if (withdraw >=1000) and (withdraw < new_balance):
                new_balance -= withdraw
                print("You have withdrawn UGX %d \n Your account balance is UGX %d" % (withdraw, new_balance))
            else:
                print("You should withdraw an amount greater than your current balance and greater than UGX 1000")
        elif reply==0:
            break
        else:
            print("UNKNOWN OPTION")
Momo()

