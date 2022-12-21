"""
# 1)program to get 2 number as input from user than display the largest among the 2 number
num1 = float(input("please enter your number:"))
num2 = float(input("please enter another number:"))
if (num1-num2 >0):
    print("{0}is greater than{1}".format(num1,num2))
elif (num2-num1 <0):
    print("{0}is greater than{1}".format(num2,num1))
else:
    print("num1&num2 both are equals")


##2)program to get 3 numbers as input from the user. Then find and display the largest among those 3 numbers.
num1 = float(input("please enter your first number:"))
num2 = float(input("please enter second number:"))
num3 = float(input("please enter third number:"))
if (num1 >= num2) and (num1 >= num3):
    print("{0}is greater than {1} and{2}".format(num1,num2,num3))
elif (num2 >= num1) and (num2 >= num3):
    print("{0}is greater than {1} and{2}".format(num2, num1, num3))
else:
    largest = num3
    print("{0}is greater than {1} and{2}".format(num1, num1, num2))


##3)Print a menu displaying the list of available items in a shop. You can decide their names and prices.

print("please input your menu 1-momo,2-chowmin,3=pasta,4=coke & 5=pizza")
int.read





## Program to get a user name and display the first name of thier first letter.
name=input("please enter your name:")
if(name[0]=="x"):
    print("this ia a intresting name")
else:
    print("it is not a intresting name")


## programs to check if the first and last characters of string are the same

name=input("please enter your first name character:")
name1=input("please enter your another name character: ")
if(name[0]==name1[-1]):
    print("the first and last character of string are same")
else:
    print("the first and last charcters of strings are not same")



## program to print each character in a string
word=input("enter a word:")
for character in word:
    print(character)


## program to replace all the "a" in the strings with"_"
word=input("enter any words:")
print(word.replace("a","_"))



## program to get user name and give a alternative character
name=input("please enter your name:")
print(name[0:7:2])


## program to get username and change alternative character to lower and upper case respectively
name=input("please enter your name :")
for i in name:
    if name.isupper():
        name+=name.lower()
    else:
        name+=name.upper()





## program to print character at even idex only.


## program to count a vowels in given name
name = input("please enter a name:")
count = 0
vowels = 'aeiou'

for i in name:
        if i in vowels:
            count+=1

print("count of the vowels is:")
print(count)



name=input("please enter your name:")
print(name[0:7:2])

 """


name = input("please enter a name")
if(name[0] =="x"):
 print("It is a intresting name")

else:
    print("it's not intresting name")


