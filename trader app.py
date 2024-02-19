print ("welcome to our store, we have these products, how can we help you today")
#list commodity and their unity prices
product={
"orange":20, 
"mango": 10,
"pawpaw":25,
"apple":15,
"yam" : 50
}
print ("(1).orange=20, \n (2).mango=10, \n (3).pawpaw=25, \n (4).apple=15, \n (5).yam=50" )
print ("which do you want ?")
product = str (input (">>")).lower()
print(f"you chosed {product}")
print ("how many do you want?")
qty = int(input())
print(f"you want{qty}")
cost = qty * product
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



