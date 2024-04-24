fruit=["apple","banana", "training", "orange","tech","tuesday", "Thursday"]
index=0

while index<len(fruit):
    if fruit[index].startswith("t") or fruit[index].startswith("T"):
    #if fruit[index][0]=="t" or fruit[index][0]=="T":
        print (fruit[index])
    index +=1
        
    