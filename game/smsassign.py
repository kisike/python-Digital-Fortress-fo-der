import sys


while True:
    print( " dial 102 to initiate transaction")
    reply=int(input(' >> '))
    if reply == 102:
        print("choose your request/n 1. buy airtime, /n 2. buy data, /n 3.make a transfer, /n 4.pay for utility, /n5. check your acc balance")
    response= int(input("enter >>"   ))
    if response==1:
        print("enter your amount and network")
        amt=input ("amount is  >    " )
        nt=input("network is  >  " )
        print(f" you want {nt} for {amt} which will be deducted from your acc /n 1. ok to cont /n 2. cancel" )
        response2=int(input(">> "))
        if response2==1:
            print("transaction successful")
        elif response2== 2:
            print("transaction terminated")
            break
    elif response==2:
         print("enter your amount and network")
         amt=input ("amount is  >    " )
         nt=input("network is  >  " )
         print(f" you want {nt} for {amt} which will be deducted from your acc /n 1. ok to cont /n 2. cancel" )
         response2=int(input(">> "))
         if response2==1:
            print("transaction successful")
         elif response2== 2:
            print("transaction terminated")
            break
    elif response==3:
        print("enter your designated bank account and amount")
        bank_acc=input ("bank account is  >    " )
        amt=input("amount is  >  " )
        print(f" you want {amt} transfered to {bank_acc} which will be deducted from your acc /n 1. ok to cont /n 2. cancel" )
        response2=int(input(">> "))
        if response2==1:
            print("transaction successful")
        elif response2== 2:
            print("transaction terminated")
            break
    elif response == 4:
        print("which utility do you want /n 1.bills/n2.remitta/n3. other")
        utility=input ("utility is  >    " )
        amt=input("amount is  >  " )
        print(f" you want to pay for {utility} with #{amt} which will be deducted from your acc /n 1. ok to cont /n 2. cancel" )
        response2=int(input(">> "))
        if response2==1:
            print("transaction successful")
        elif response2== 2:
            print("transaction terminated")
            break
    elif response==5:
        print("enter your pin")
        pin=input ("   >    " )

        print(f" to check your balance /n 1. ok to cont /n 2. cancel" )
        response2=int(input(">> "))
        if response2==1:
            print("transaction successful")
        elif response2== 2:
            print("transaction terminated")
            break
    else:
       print("ooops!")
    SystemExit