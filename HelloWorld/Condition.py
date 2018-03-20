#answer = input("Would you like express shipping? ").lower()
#if answer == "yes"  :
#    print("That will be an extra $10")
#elif answer == "no" :
#    print("That will be all")
#else :
#    print("Sorry i dont understand what you are saying")

deposit = int(input("How much do you want to deposit? "))
if deposit >= 100 :
    print("You are eligible to deposit");
elif deposit < 100 :
    print("Minimum of 100 is required")
else :
    print("I don't understand what you typed in");
print("Have a nice day")