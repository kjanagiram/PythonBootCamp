from random import shuffle,randint

print("Looping statement")

for i in [1,2,3,4,5,6]:
    print(i)

mylist=[1,2,3,4,5,6,7,8,33,44,55,11,65,43,78,-1]
sum=0
for item in mylist:
    sum+=item

print(f"Sum of {mylist} value is {sum}")
print()
sum=0
for item in mylist:
    if item%2==0:
        sum+=item
print(f"Sum of even number in {mylist} is {sum}")

myname="Hitache"

for ch in myname:
    print(ch)

tup=(9,8,7,6,5,4,3,2,1)
for t in tup:
    print(t)

tup=[(1,2),(3,4),(5,6),(7,8),(9,10)]
print(f"length of the tuple {len(tup)}")
for item in tup:
    print(item)

sum1=sum2=0
for (a,b) in tup:
    sum1+=a
    sum2+=b
print(f"sum of tuple values {sum1} and {sum2}")


dictionary={'name':'janaki','age':22,'address':'north mettu street'}

for key,value in dictionary.items():
    print(key+':'+str(value))

for value in dictionary.values():
    print(value)
'''
While loop Syntax
#1 while condition:
    statement
#2 while condition:
    statement
   else:
     statement
'''
x=0
while x<5:
    print(x)
    x+=1

print()
y=5
while y>1:
    print(y)
    y-=1;
else:
    print(y)

num=123
sum=0
r=0
print()
while num!=0:
    r=num%10
    sum+=r
    num=num//10

print(sum)

'''
break statement -  used to break a loop
pass statement  -  do nothing 
continue statement - continue the loop from the beginning
'''
x=0;
while x<6:
    if x==2:
        x+=1
        continue
    if x==4:
        break
    print(x)
    x+=1
else :
    pass
    print("end")


name= input('enter a name')
print(name)

#name= input('enter a name')
#print(name)

'''range operators. It does not include last value. In our example 10.
syntax:
    range(start, end, [step]) 
step is optional
'''
print(list(range(0,10)))

mylist=list(range(0,10))
print(mylist)

for item in range(0,10):
    print(item)

mylist1=list(range(0,11,2))
print(mylist1)
for item in mylist1:
    sum+=item
print(sum)

#enumerator
word='janakirarman'
for pos,value in enumerate(word):
    print(str(pos)+"-->"+value)

#zip operator

list1=[1,2,3,4]
list2=[10,100,100,1000]
list3=['ja','na','ki','k']

print(list(zip(list1,list2,list3)))
print()
zippedvlaue=list(zip(list1,list2,list3))

for z in zippedvlaue:
    print(z)

for x,y,z in zippedvlaue:
    print(str(x)+"-->"+str(y)+"-->"+z)

#suppose any of the below list is uneven,
# it will not produce an error.
# It will only consider shortest list while performing zip
list1=list(range(0,10))
print(list1)
list2=[10,100,100,1000]
list3=['ja','na','ki','k']
zipp=zip(list1,list2,list3)
for z in zippedvlaue:
    print(z)

# "in" operator
#used to find whether specific item is present in the list of values
#if it presents, it will return True, otherwise False
print('x' in 'xyz')
print('x' in ['x','y','z'])
print( f"11 in {list(range(0,10))} - {11 in list(range(0,10))}")
print( f"1 in {list(range(0,10))} - {1 in list(range(0,10))}")

d={'k1':123,'k2':564}

print(f"k2 in d {'k2' in d}")
print(f"564 in d {564 in d.values()}")

# min and max operator
print(min(list(range(10,1000,3))))
print(max(list(range(10,1000,3))))

mylist=list(range(1,12))
print(f"List before shuffle {mylist}")

#need to import shuffle, randint from the random library to work with shuffle() and randint() functions.
# in this, it was import in the top of the file
#shuffle is "inplace". means, shuffle is happening within the list.
# it will give output as None. it will not return new list
shuffle(mylist)
print(f"List after shuffle {mylist}")

print(randint(0,100))

'''input - used to get the user input
It will alwasy read a user input as a string. 
We need to cast the user input based on our need
'''
name=input("Enter your name")
print(name)
'''
Either we can cast the value after getting the input from the user (#1)
or
cast and assigne to a variable when by wrapping the input() function by the the type as you need (#2)
ex :  int(input("Enter your age"))
'''
#1
age=input("Enter your age ")
print(age)
print(type(age))
age1=int(age)
print(type(age1))

#2
mark=int(input("Enter your mark"))
print(mark)
print(type(mark))

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split(' '):
    #print(word+"-->"+str(word.find('s')))
    if word.find('s') == 0:
        print(word)

#Use range() to print all the even numbers from 0 to 10.
for r in range(0,10,2):
    print(r)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
listcompre=[x for x in range(1, 50) if x % 3 == 0]
print(listcompre)

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) %2 == 0:
        print(word)

'''
Write a program that prints the integers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".'''

for x in range(1,100):
    if x % 3 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

firstletter = [index[0] for index in st.split()]
print(firstletter)

