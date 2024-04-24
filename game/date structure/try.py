# tunde=10
# try:
#     print(tunde)
# except:
#     print("tunde is not defined")
# else:
#     print("nothing went wrong")
# finally:
#     print("the prgram ends here")

# try:
#     tunde=open("tunde.txt","x")
#     try:
#         tunde.write("here we stand")
#         # you can also use tunde=open(../tunde.txt) or (//tunde.txt) to locate created file
#     except:
#         print("something when wrong wuth the creation")
#     else:
#         print("file was created succesfully")
# except:
#     print("something went wrong with the creation")
# finally:
#     print("the logic is done running")
# # u can also use tunde.close to close the file created

# tunde=open("tunde.txt","r")
# print(tunde.read)

# tunde= open("tunde2.txt","a")
# tunde.write("we are in class")
# tunde.close()
# # u can use "w", "x"

tunde=open("tunde2.txt" ,"r")
print(tunde.read())
tunde.close()

# import os
# os.rmdir(tunde)