print ("welcome to our store, how may we help you, we have the following products")
print ("coke, pepsi, fanta, 7up")
coke = 150
pepsi = 200
fanta = 150
sevenup = 250
cp = coke+pepsi
cf = coke +fanta
cs = coke + sevenup
pf = pepsi + fanta
ps = pepsi + sevenup
fs = fanta + sevenup
cpf = coke + pepsi +fanta
cps = coke+ pepsi+sevenup
cfs = coke + fanta + sevenup
pfs = pepsi + fanta +sevenup
cpfs = coke+pepsi+fanta+sevenup
print ("which product(s) do you want to purchase ?")
print ( "(1):coke,\n(2):pepsi, \n(3):fanta, \n(4): sevenup, \n(5):cp, \n(6):cf,\n(7):cs,\n(8):pf,\n(9):ps,\n(10):fs, \n(11):cpf, \n(12): cps, \n(13): cfs, \n(14): pfs, \n(15): cpfs ")
response= str(input ( ">> ")).lower()
print(response)
if response =="coke" or response == "1":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = coke*quantity
    print(f"your total cost is {total_cost}")
elif response =="pepsi" or response == "2":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = pepsi*quantity
    print(f"your total cost is {total_cost}")
elif response =="fanta" or response == "3":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = fanta*quantity
    print(f"your total cost is {total_cost}")
elif response =="sevenup" or response == "4":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = sevenup*quantity
    print(f"your total cost is {total_cost}")
elif response =="cp" or response == "5":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = cp*quantity
    print(f"your total cost is {total_cost}")
elif response =="cf" or response =="6":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = cf*quantity
    print(f"your total cost is {total_cost}")
elif response =="cs" or response == "7":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = cs*quantity
    print(f"your total cost is {total_cost}")
elif response =="pf" or response == "8":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = pf*quantity
    print(f"your total cost is {total_cost}")
elif response =="ps" or response == "9":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = ps*quantity
    print(f"your total cost is {total_cost}")
elif response =="fs" or response == "10":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = fs*quantity
    print(f"your total cost is {total_cost}")
elif response =="cpf" or response == "11":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = cpf*quantity
    print(f"your total cost is {total_cost}")
elif response =="cps" or response == "12":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = cps*quantity
    print(f"your total cost is {total_cost}")
elif  response =="cfs" or response == "13":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = cfs*quantity
    print(f"your total cost is {total_cost}")
elif  response =="pfs" or response == "14":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = pfs*quantity
    print(f"your total cost is {total_cost}")
elif response =="cpfs" or response == "15":
    print("what quantity do you need ?")
    quantity=int(input())
    print (quantity)
    total_cost = cpfs*quantity
    print(f"your total cost is {total_cost}")
print ("you get 1% discount if total_cost is > 1000")
discount = total_cost * 1/100
final_cost = total_cost - discount
if total_cost > 1000 :
    print(f"your cost is {final_cost}")
else:
    print(f"your cost is {total_cost}")
print("how do you want to pay")
print("a.cash, \n b.electronic")
pay_method = (input (">>")).lower()
print (pay_method)
if pay_method == "cash" or pay_method =="a" : 
    print("lets have your cash")
elif pay_method =="electronic" or pay_method == "b" :
    print("POS or bank transfer")
else:
    print ("choose a payment method")
    print("invalid response, enter valid respose")
print("thanks for your patronage 😍")