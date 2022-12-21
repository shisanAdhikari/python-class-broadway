"""
## 1)programs to get input from user and display greetings
name=input("please enter your name:")
print("Namaste"+name)

## 2)programs to get numeric input from user and converting it to a number;
num=int(input("please enter your number:"))
print(num)


## 3)programs to get two numeric inputs from the user and displaying their product,sum and difference.
print("please enter n1: ")
num1=int(input())
print("please enter n2: ")
num2=int(input())
#for addition
add=num1+num2
print("the sum of given number is"+str(add))
#for substraction
sub=num1-num2
print("the difference of given number is"+str(sub))
#for multipication
product=num1*num2
print("the product of given number is"+str(product))
#for division
div=num1/num2
print("the division of given number is"+str(div))



## 5)program to print whether a number is odd or even
num= int(input("please enter a number to check a number is odd or even:"))
if(num%2==0):
    print("{0}is even number")
else:
    print("{0}is odd number")



# program to find the age and  know how to vote or not
age=int(input("please enter your age:"))
if age>=18:
    print(age,"are able to vote")
else:
    print(age,"are not able to vote")


# program to check if a number is negative, zero  or positive
x=int(input("please enter your number"))
if x<0:
    print(x,"it gives negative number")
elif x==0:
 print(x," it is equals to zero")
else:
    print(x,"it will give positive value")


# displaying a multlipication table for given number
num=int(input("please enter any number for multipication table:"))
for i in range(1, 11):
 print(num,"*",i,'=',num*1)
 """



















