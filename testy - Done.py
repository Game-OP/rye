print ("hello, welcome to NYX Cafe")
print ("what's your name\n")
name = input("Your name >>")

print ("\nhello " + name + "!!! here's your menu\n")

print ("Table's Number")
NO = input("No>>")

print ("What's your order?")
print ("a. Cappucino")
print ("b. Black Coffee")
print ("c. White Coffee")
print ("d. Cookies and Cream\n")

ans = input("your choice>>")

if ans == "a" or ans == "A" or ans == "b" or ans == "B" or ans == "c" or ans == "C" or ans == "d" or ans =="D":
    print("your drink will be right up, You can close this tab")
else:
   print("choose another drink by closing this tab and open it again")
