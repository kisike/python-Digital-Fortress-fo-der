print("good day,welcome. what is the value of your total purchase")
total_purchase= float(input())
print("our company charges 10% of your total purchase as tip")
tip = 1/10*total_purchase
total_cost = tip + total_purchase
print ( "are you making a singular payment or joint payment")
print ("(a) singular payment")
print ("(b) joint payment")
response = input ("response  " )
if response == "a":
    print(total_cost)
    print("thanks for coming💕")
elif response == "b":
    number_of_person = int(input("number of person is "))
    cost_per_person = total_cost/number_of_person
    print(number_of_person) 
    print(total_cost)  
    print(cost_per_person) 
    print (f"each person will be paying {cost_per_person}" )
    print("thanks for coming💕")
else:
    print ("invalid response, input a valid response")
    print("thanks for coming💕")