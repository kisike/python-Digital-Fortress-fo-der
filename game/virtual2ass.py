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