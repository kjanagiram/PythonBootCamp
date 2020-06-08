'''class name always use camel case to follow the naming convention. For example 'SampleClass' or PerAnimals'''

class Sample():

    '''this is constructor in python. 'self' is a keyword, defining like the current object of a class
        --init__ is a constructor of a class. Instead of 'self' we also can use different name. But for the
        naming convention 'self' should be used to follow the python standard and other developers to understand.
        --init__ is a special method'''
    address=""
    def __init__(self,address):
        print("This constructor in python")
        self.address=address

    def print_name(self,name):
        print(f"My name is {name}")
        print(f"My name is {self.address}")

    def my_age(self, age):
        return age

    def my_tax(self,salary):
        return salary*.30

sample=Sample('123, abc address');
sample.print_name('janaki')
print(f"My age {sample.my_age(22)}")
print(f"My tax {sample.my_tax(10000)}")


