print ("welcome on board")
kano = 300
enugu = 350
ikeja = 450
ogun = 200
osun = 250
print ("where are you headed to!\n you said what?")
print (" 1.kano-300\n 2.enugu-350 \n 3.ikeja-450' \n 4. ogun-200, \n 5. 0sun-250")
response = str(input( ">> ")) .lower ()
print (response)
print ("please hold your pesonal belongings and change dearly !") 
print ("how much are paying with ?")
reply = int (input ())
if reply < 500 :
    print (f"ok {reply}")
    print ("enter \n driver to the next stop !")
    if response== "kano" or response == "1":
        bal = reply - kano
        if bal == 0:
            print (" you donot have change")
        else:
         print (f" your change is {bal}")
    elif response == "enugu" or response == "2":
        bal = reply - enugu
        if bal == 0:
          print ("you donot have change")
        else:
           print (f"your change is {bal}")
    elif response == "ikeja" or response =="3":
        bal = reply - ikeja
        if bal == 0:
           print ( "you donot have change")
        else :
           print (f"your change is {bal}")
    elif response == "ogun" or response == "4":
        bal = reply - ogun
        if bal == 0 :
           print (" you donot have change")
        else :
           print (f"your change is {bal}")
    elif response =="osun" or response =="5":
       bal = reply - osun
       if bal == 0:
          print (" you donot have change")
       else :
          print (f"your change is {bal}")
else :
   print (" i donot have change oo! \n until we can find change \n drive please move.")
