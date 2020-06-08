class Animals():
    def __init__(self):
        print('Generic class')

    def name(self,name):
        print(name)

class Cat(Animals):
    def __init__(self):
        Animals.__init__(self)
        print("This is cat")

    def eat(self):
        print("I eat milk")


cat =Cat()
cat.eat()
cat.name('cat')

print(getattr(cat,'name'))