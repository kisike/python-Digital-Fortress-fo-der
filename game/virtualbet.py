import random

# team1_score = 0
# team2_score = 0
# rounds = 5  # Number of rounds

# round_number = 1
# while round_number <= rounds:
#     # Generate random scores for both teams for each round
#     team1_score += random.randint(0, 5)
#     team2_score += random.randint(0, 5)
    
#     print(f"Round {round_number}:")
#     print(f"Team 1 score: {team1_score}")
#     print(f"Team 2 score: {team2_score}")
#     print()  # Empty line for readability
    
#     round_number += 1

# print("Game over!")
# print("Final scores:")
# print(f"Team 1: {team1_score}")
# print(f"Team 2: {team2_score}")


a= range (2,7)
b= range(3,5)
for i in a:
    for j in b:
        a=input()
        b=input()
        guess=input("guess  >  ")
        print(f'{i} - {j}')
        if guess==print:
            print("correct") 