def main ():
     passwords = {}
     while True:
        print("password management system")
        print("1.store password, \n 2.retrive password, \n 3.Exit")

        choice=input("enter your choice:   ")


        if choice== '1':
            website=input("enter website:    ")
            password=input("enter password:    ")
            passwords[website] = password
            print("password stored successfully")
                  
        elif choice =='2':
            website=input("enter website:   ")
            if website in passwords:
                password=passwords[website]
                print("password for", website, "is:",passwords[website])
            else:
                print("passsword not found for", website)
        elif choice=='3':
            print ("exiting")
            break
        else:
            print("invalid choice! try again")

