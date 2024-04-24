x=5
y=6
for x in range (0,5):

  print(f"{x} x {y} = {x*y}")


  mynumber=int(input("enter your number >>  "))
  for i in range(0,12):
    print(f"{mynumber}*{i}={mynumber*i}")

    x=5
    for i in range (0,x+1):
      for tunde in range(1, x+1):
        #print ("tunde")
        product=i*tunde
        print (f"{product:4}", end= "\t")
        print()


