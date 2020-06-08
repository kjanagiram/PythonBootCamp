'''if a variable is declared with __ in the class, then the data is hiding automatically by python.
    Like private variable in Java'''
class Abstraction():
    __count=0;
    def __init__(self):
        print("")

    def increement(self):
        self.__count+=1;
        return self.__count

ab=Abstraction()

'''
This line will throw an error like ''Abstraction' object has no attribute '__count'. 
Since we cannot access the variable from the outside of the class
'''
# print(ab.__count)

print(ab.increement())
print(ab.increement())


