"""
Task 0: Class We-Do
"""

from typing import Any


class Character:
    health = 20

    def __init__(self, name):
        self.name = name

    def damage(self, dmg):
        self.health = self.health - dmg

class Player(Character):
    health = 50

    def heal(self): 
        if self.health < 50:
            self.health =  self.health + 1
enemy1 = Character("Balthazar")
enemy1.damage(1)
print(enemy1.health)

player1 = Player("Rgjmerc")
player1.heal
print(player1.health)


"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

class Person:
    def __init__(self, name, age):
        #the actual way to get the class to have attributes
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
person1 = Person("Cycil", 18000000000)
print(person1.introduce())

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class cat:
    def speak(self):
        print ("Lasagna")
class dog:
    def speak(self):
        print ("Raggy?")
Scooby = dog()
#giving the function a connection so it can work
Scooby.speak()
Garfield = cat()
Garfield.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class Bank_Acc:
    def __init__(self, owner, balance = 200000):
        self.owner = owner
        self.balance = balance
    def deposit(self,deposit):
        self.deposit = deposit
        self.balance = self.balance + self.deposit
        #depositing into accounts
    def withdraw(self,withdraw):
        self.withdraw = withdraw
        self.balance = self.balance - self.withdraw
        #withdrawl from accounts
Jerry_Steinfield = Bank_Acc("Jerry")
#setting the accout to a name/owner
Jerry_Steinfield.withdraw(100000)
print(Jerry_Steinfield.balance)
Jerry_Steinfield.deposit(900000)
print(Jerry_Steinfield.balance)