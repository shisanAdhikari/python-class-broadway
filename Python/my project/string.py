
"""
#Prints name variable;
#name= "Barnit"
#print(name);
### Looping through string

#This statement loops through each letter of banana
#and adds each letter to x one by one in each iteration
#of the loop
#for in "banana":
  # print(x)

## int function
##It refers to the number whole number without decimals,or simply a number.
x=20202121
print(type(x))
##here we can know that this shows a this is a int or helps to know the types of variables.
y="shisan adhikari"
print(type(y))
## how to find the length of tne variables from string
pharse="congrulations"
print(len(pharse))
#we can find the number of each letters by the alphebet
pharse="congrulations"
print(pharse[3])
#similarlly we can find the single aphabet of others too.

## Index function- this function is used to know where the specific character and string is located.
#this function give us a numbers from alphabet.
pharse="congrulations"
print(pharse.index("u"))
## simallary we can find the index numbers of the whole sentence or the one word.

##Replace function- this function replace the one sentence or the one  word with others.
Pharse ="congrulations"
print(pharse.replace("gru" ,"aru"))
## like  this we can replace whole sentence too.


## Working with numbers
print(9696969)
print(9*9*9-100)
## we can do any kinds of mathematical operations using python..

## function using  numbers
##Absolute value (abs)= we can find the absolute value using this function.
My_number=-55
print(abs(My_number))
##power(pow)=this function has two function one is number and another is power of it.
my_number=55
print(pow(2,6))
## max function=this function shows a max/greater number bettwen a numbers.
print(max(44,50))
## min function=this function shows a minimum/ small number betwween a numbers.
print(min(66,30))
# round function=This function round the number nearer to the whole number.
print(round(3.3))
print(round(3.7))
# in this example we can see that 3.3 shows 3 while round &4 is shown while 3.7 is rounding.

#ceal function-This function round up the decimal increases the number.
My_number=8
print(ceil(3.2))


from math import*

##Square root function(sqrt)= this function helps tyo give a square root of the numbers.
print(sqrt(36))

##### Geeting input from users = this fuction helps to allowc to gets inputs from someone.
# we have to input the fuction and python will allows to input the  information.
name=input("please enter your name:")
age=input("please enter your age:")
print("hello"+name+", you are "+age+"!")
# like this we can input various variables .


### Building a basic calculator= we can do the calculation from python by using int for whole num & float for dec num.
num1=input("please enter your numbers:")
num2=input("please enter your another numbers:")
results= int(num1)+int(num2)
print(results)
# similarly we can do the calculation of dec number by using a float variables
num1=input("please enter your numbers:")
num2=input("please enter your another numbers:")
results= float(num1)+float(num2)
print(results)

#### mad libs game= this is a type of game in which we enter abunch of words in it.and make it attractive by usingh own lines
colour=input("please enter your colour:")
noun=input("please enter a noun:")
hero=input("please enter your hero:")

print("roses are" + colour)
print(noun + "is blue")
print("hari loves" + hero)

#we can made a mad libs games like this  by adding a sentence.



#### Lists= lists are made to store a bunch of information in the  python.than lists track allof them when we keep on list.
# it will modify values inside a list.
friends=["hari","shyam","ram", "mohan"]
print(friends[2])
# like this we can find from a number  after making a lists.


# Lists function= in this function we can store a two different bunch of  different function in a same bunch.
best_numbers=[12,22,20,23]
friends =["Sumi", "Samjhu","Ram", "Ramhari", "Mohan"]
friends.extend(best_numbers)
print("friends")


#extend function=in this fuction we can add both  types of lists toghether.

## insert function= in this function we can add a elements on it
best_numbers=[12,22,20,23]
friends =["Sumi", "Samjhu","Ram", "Ramhari", "Mohan"]
insert(1,son)
print("friends")


## simallarly we can remove a ellements or words  which can be called remove function. we can write which element we want to remove.
best_numbers=[12,22,20,23]
friends =["Sumi", "Samjhu","Ram", "Ramhari", "Mohan"]
friends.remove("Sumi")
print("friends")

## clear function= this function allows to  clear all the elements and shows the empty  file.
best_numbers=[12,22,20,23]
friends =["Sumi", "Samjhu","Ram", "Ramhari", "Mohan"]
best_numbers.clear()
print("best_numbers")

## Tuples= it is a  types of data structure which we can store a different values.iit can be called container
# tuples cannot be changed or modified once created it can't be changed .

 coordinates = [(4,5),(2,6),(5,7)]
 coordinates[1]=10
 print(coordinates[1])

# tuples can be used as a data that never be changed.



# function= collection of codes which performs a specific tasks, it helps to break down a codes and many more.
## def is a key word for function which means the users wants to  use function.
def say_hi(name):
    print("Hello"+name)


say_hi ("Hero")
say_hi ("handsome")

#we can pass th e2 pieces of the information fron the function lioke
def say_hi(name,age):
    print("Hello"+name,"you are" +age)


say_hi ("Hero","36")
say_hi ("handsome","22")


## Return statement= it allows the return information from a function

#  finding a cube of the numbers
def cube(num):
    return num*num*num


print(cube(3))
      ## return statement helps to return the value  in the above   example / it can return evcerthings in an every conditions.

#If statement= this statements is used to make a decisions. it can be either true or false too according to a conditions.
is_male=True
is_tall=True

if is_male or is_tall :
      print("you are a male or tall or both")
else:
  print("you are neither a male nor tall")


  ## elseif statement(elif)= elif condition is used to include multiple conditional expressions after the if condition or between the if and else conditions.

is_male=True
is_tall=False

if is_male or is_tall :
      print("you are a male or tall or both")

elif is_male and not(is_tall):
    print("you are a smaller male")
elif not(is_male)and is_tall:
    print("you are tall male")


else:
  print("you are neither a male nor tall")



  ## If statements and comparision = instead of using boolen value we can  compare different numbers& strings. by using comparision operators.

def greater_numbers(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    print(greater_numbers(200,201,400))
    # then greater number  will be seen.


   ### Building a better calculator = in this calculator we can perform all kinds of arthmatics calculations

num1= float(input("please enter a number"))
op=input("enter operator")
num2=float(input("please enter another number"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)

else:
    print("invalid operators")

    ## similarly we can do by using others operators also.


### Dictionaries= in this  portion we can knowhow to run dictionary in python.
    # months conversions= in this  we can  convert the 3 letters to the full name of the months.

Monthsconversions =  {

        "jan":"January",
        "feb":"February",
        "mar":"March",
        "apr":"April",
        "may":"May",
        "jun":"June",
        "july":"July",
        "aug":"July",
        "sep":"September",
        "oct":"October",
        "nov":"November",
        "dec":"December"


    }

print(Monthsconversions.get("oct"))

### in this small form is it's key & full name is it's value.& we can use any kinds of data types as a key to find out it;s value.
#  we can use  this conversion by using.get or  by [] brackets




## While loop= this loops alows us to loop  through  block of codes with multiple times.
# It will execute continiously until the statement become false.

i=1
while i<=10:
        print(i)
        i+=1



        print("done with loop")
        

### Building a guiessing game= in this game we can make a simple guiessing game  by keeping the  word sectret

secret_word="looping"
 guess""
guess_count=0
guess_limit=3
out_of_guesses=false


while guess!=secret_word and not(out of gusses):
    if guess_count< guess_limit:
    guess=("input guess")
    guess_count=+1
    print("you win")
else:
    out_of_guesses=true
if_out_of_gusses:\
print("out of gusses,yoy lose")
# in gtis game we use the while loop & for loops.
"""""

# For loops= it allows to loop over the different collections of items , we can lloop over arrays, letters in strings, series of numbers.
## It may be have different values each times.

for letters in"london":
    print(letters)

































