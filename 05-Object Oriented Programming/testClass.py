class Animal:
    def __init__(self):
        print('Animal Created')
    def who_am_i(self):
        print('I am an ANIMAL')
    def eat(self):
        print('EAT!!')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
    def who_am_i(self):
        print('Woff Woff')
    print('Dog Created')

class Cat(Animal):
    
    def __init__(self, my_name):
        Animal.__init__(self)
        self.name = my_name
    def who_am_i(self):
        print(self.name+'thats my name!!')    
    print('Cat Created')
nala = Dog()
nala.eat()
nala.who_am_i()

felix = Cat('felix')
felix.who_am_i()

