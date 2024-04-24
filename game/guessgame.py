import sys

while True:
    game=["2,0", "3,2","2,1", '0,0', "1,1"]
    index= 0

    print("guess the score of the game")
    response=input(f"what is the game score for game[0]  \n")
    if response == (game[0]):
        print("congratulations")
    
    else:
        print (f"wrong , the score is")
        print(game[0])
         
    print("guess the score of the next game")
    response=input(f"what is the game score for game[1]  \n")
    if response == (game[1]):
        print("congratulations")
        
    else:
        print (f"wrong , the score is")
        print(game[1])
        
    print("guess the score of the next game")
    response=input(f"what is the game score for game[2]  \n")
    if response == (game[2]):
        print("congratulations")
        
    else:
        print (f"wrong , the score is")
        print(game[2])
        
    print("guess the score of the next game")
    response=input(f"what is the game score for game[3]  \n")
    if response == (game[3]):
        print("congratulations")
        
    else:
        print (f"wrong , the score is")
        print(game[3])
        
    print("guess the score of the next game")
    response=input(f"what is the game score for game[4]  \n")
    if response == (game[4]):
        print("congratulations")
        
    else:
        print (f"wrong , the score is")
        print(game[4])
        congratulation=[]
        for congratulation in game ():
          congratulation =0 
          congratulation +=1
          print()

          
    print(f"total game won is {congratulation}")
    break



