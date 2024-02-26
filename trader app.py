print ("welcome to our store, we have these products, how can we help you today")
#list commodity and their unity prices
orange= 20
mango= 10
pawpaw= 25
apple= 15
yam= 50
print ("(1).orange=20, \n (2).mango=10, \n (3).pawpaw=25, \n (4).apple=15, \n (5).yam=50" )
print ("which do you want ?")
product = str (input (">>")).lower()
print(f"you chosed {product}")
if product == "orange" or product == "1":
   print ("how many do you want?")
   qty = int(input())
   print(f"you want{qty}")
   cost = qty*orange
   print(f"your price is {cost}")
elif product == "mango" or product == "2":
   print ("how many do you want?")
   qty = int(input())
   print(f"you want{qty}")
   cost = qty * mango
   print(f"your price is {cost}")
elif product == "pawpaw" or product == "3":
   print ("how many do you want?")
   qty = int(input())
   print(f"you want{qty}")
   cost = qty * pawpaw
   print(f"your price is {cost}")
elif  product == "apple" or product == "4":
   print ("how many do you want?")
   qty = int(input())
   print(f"you want{qty}")
   cost = qty * apple
   print(f"your price is {cost}")
elif product == "yam" or product == "5":
   print ("how many do you want?")
   qty = int(input())
   print(f"you want{qty}")
   cost = qty * yam
   print(f"your price is {cost}")
print ("you get 1% discount if cost is > 1000")
discount = cost * 1/100
final_cost = cost - discount
if cost > 1000 :
    print(f"your cost is {final_cost}")
else:
    print(f"your cost is {cost}")
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


