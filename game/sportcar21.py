
car_moving = 0

while car_moving < 5:
    command=()
    command = input("> ")
    if command == "start":
        print("game started")
        car_moving += 1
        print("car is running     "  *5 )
    if command=="stop":
        print("car stopped")
    if command=="turn left":
            print("car has turned left")
    if command == "turn rigth":
            print("car has turned rigth")
    if command =="speed":
           print("car is speeding up  " *3)
    if command==("brake"):
          print("car on brake")
    
else:
    print("Invalid command. Please enter 'start' to begin the game.")

print("The car has run 5 times. Game over")