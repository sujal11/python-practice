from turtle import color


class Animals:
    animalType="Mammal"

class Pet(Animals):
    color="white-brown"

class Dog(Pet):
    @staticmethod
    def bark():
     print("bow bow!!")

D=Dog()
D.bark()