class Animal:

    def move(self):
        print('Animal is moving')

class Dog(Animal):

    def move(self):
        print('Dog is running')

    def parentMove(self):
        print('Call parent method')
        Animal.move(self)

a = Animal()
a.move() # call Animal.move

d = Dog()
d.move() # call Dog.move
d.parentMove() # call Dog.parentMove
