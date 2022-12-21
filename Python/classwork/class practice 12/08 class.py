"""
class Coordinates:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

    def __str__(self):


number= random.randint(0,10)
n_guess=3
for i in range(n_guess):
    guess=int(input("please enter a number:"))
    if guess == number:
        print(f" {number} is the right guess!! you won!!!!")

    elif guess >number:
        print("your guess is too high!!")

    else:
        print("your guess is too low!! ")
        print(f"the number is {number}")

"""

'''Class Definition Start'''
class Person:

  def __init__(self,name,age):
    self.name=name
    self.age=age

def say_name(self):
   print(f"Hello,my name is {self.name}!")

def say_age(self):
  print(f" it's same to say a age but, i am {self.age}!")
'''Class definition End'''


Ram = Person("Ram Karki",15)
Hari = Person("Hari Basnet",26)

Ram.age = 26
Ram.address = "Itahari"
print(Ram.__dict__)
print(Person.__dict__)
