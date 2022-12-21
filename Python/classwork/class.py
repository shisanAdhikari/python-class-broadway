"""
# program to  calculate the square of each number from 1 to n.
n=20
count=0
for i in(1,11):
    n=i*i
    count+=1
    print(n)




num=0
while num<=100:
    print(num)
    num=num+2



# by using while loop program to  calculate the square of each number from 1 to n.
n=20
m = 1
while m<=n:
    print(m**2)
    m = m + 1



n=1
fact=0
while n<=10:
    fact=fact*n
    print(fact)
    n = n+1


# program to find the factriols:
n=5
fact = 1
for i in range(1, n+1):
    print("fact:", fact, "i=", i)
    fact = fact * i
    print(fact)



n=int(input("please enter your number:"))
a = []
for i in range(n):
    stds_name = input("enter a student name:")
    a.append(stds_name)
print(a)




my_list=[1,2,3,4,5,6,7]
my_list.append(8) #appending 8
print(my_list)

my_list.remove(3) # removing 3
print(my_list)



## Find the factors of a given number. The factors of a number "n" are all the numbers which divide "n" exactly.

n = int(input("please enter a number for factors:"))
for i in range (1,n+1):

  if(n%i==0):
    print(i)




##

# program to print the all odd intigers from 1 to n
number=int(input("please enter a number:"))
for number in range(1, number + 1):
    if(number % 2 != 0):
        print(number)


import random

# program to print the all prime intigers from 1 to n
"""
import random

number=int(input("please enter a number:"))
num_is_prime = True
"""
list = [1,2,3,4,5,6,7,8,9]
tuple = (1,2,3,4,5)
count = 0
for n in tuple:
    for m in range(5,10):
        for p in range(7,9):
            count = count + 1
            print("Count" + " " + str(count))

    
    print(n)

for number in range(2, number):

    rem = n % 1
    if rem ==0:
        print("number is composite")
        number_is_prime = False
        break
         if number_is_prime:
            print("number is prime")

"""

## Gussing game

number = random.randint(0,10)
n_guess = 3
for i in range(n_guess):
    guess = int(input("Guess the number:"))
    if guess == number:
        print(f"you won! the number was {number}")
        break
    elif guess > number :
        print("your guess is too high!")
    else:
        print("your guess iS too low!")
        print(f"the number was {number}.")
        





