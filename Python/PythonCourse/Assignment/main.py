### Check if the entered number is divisnle by 7 or not;



def CheckIfNumberIsDivisibleBySeven():
   entry=input("please enter your number")
   number=int(entry)
   reminder:int=(number%7)
   if reminder=0:
    print("the number is divisible by 7")
    else:
        print("the number is not  divisible by 7")

CheckIfNumberIsDivisibleBySeven()