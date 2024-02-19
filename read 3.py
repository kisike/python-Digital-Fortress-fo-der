print (" Welcome here, the follow will be rquired of you")
print(" first name", "last name" ,"user name" , "pass word" ," gender" )
first_name =str(input("first name is  "))
last_name = str(input("last name is   "))
user_name = str (input ("user name is  "))
print  ("are you a male or female")
print  ("(a) you are a male ")
print  ("(b) you are a female ")
response = input ("response   ") 
if response == "a":
    print ("you are a male")
elif response == "b": 
    print  ("you are a female")
else :
    print  ("prefer not to mention") 
password_1 = str,int (input("pass_word_1  " ))
password_2 = str,int (input ("pass_word_2   "))
if password_1 == password_2:
    pass
else:
    print("password does not match")

print(f"{user_name}, your account was created successfully")
      





