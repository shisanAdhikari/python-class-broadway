"""
string="racecar"
string1=(string[::-1])
if string==string1:
    print("it is palindrome")
else:
    print("it is not palindrome")



n=20
for i in range(1,20):
    print(i)



## program to print the all odd intigers from 1 to n
number=20
for number in range(1, 20 + 1):
    if(number % 2 != 0):
        print(number)


##program to print all the even intigers from 1 to n
n=20
for n in range(0,20+1):
    if(n % 2 !=0):
        print(n)


## program to Print the middle character of a string.

name=input("please enter a name:")
print("original_string:",name)
print("middle_char:"middle_char(name))



## program to Read n numbers from the user and display the average.
n = int(input("Enter number:"))
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)

"""

