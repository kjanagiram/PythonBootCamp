print("Methods and Functions")

'''
By using def keyword, we can declare a function in python. Below are the syntax of different functions 

syntax
#1 Basic function
def function_name():
    statement

#2 Function with return value
def function_name():
    return value
    
#3 Function with arguments  and return value
def function_name(args):
    statement
    return value

#4 Function with default argument 
def function_name(arg=value):
    statement 
'''
def basic_function():
    '''
    DOCSTRING : THIS IS BASIC FUNCTION
    INPUT : NO INPUT
    OUTPUT : NO OUTPUT
    :return:
    '''
    print("This is basic function")

basic_function()

# help(basic_function())

def is_present():
    if 'a' in 'aeiou':
        return True
    else:
        return  False
print(is_present())

def is_greater(x,y):
    if x > y:
        return x
    else:
        return y

print(is_greater(10,12))

def show_name(name='Janaki'):
    return "Hi ! "+name

print(show_name())
print(show_name('Ram'))

'''
*args and **kwargs

*args - to pass arbitrary number of argument, we can use *args in a method argument
def func_name(*args):
    statement

**kwargs - to pass key word argument to a method we can use **kwargs in a method argument
def fun_name(**kwargs):
    statement
'''

def arbitrary_arg(*args):
    add = 0
    print(args)
    for item in args:
        add+=item
        print(item)
    return add

sum1=arbitrary_arg(20,30,54,85,61,75)
print(sum1)

def keyword_arg(**kwargs):
    print(kwargs)
    for item in kwargs:
        print(item)

    for item in kwargs.values():
        print(item)

keyword_arg(k1='2',k2='3')

def combine_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print(args[2])
    print(kwargs['orange'])

combine_args_kwargs(1,2,3,4,5,banana=100,apple=200,orange=150,fig=120)

def myfunc(*args):
    mylist=[]
    for item in args:
        if item%2==0:
            mylist.append(item)
    return mylist

print(myfunc(1,2,3,4,5))

def transpose(word):
    t=''
    for index,value in enumerate(word):
        if index % 2 == 1:
            t=t+word[index].lower()
        else:
            t=t+word[index].upper()
    return t

print(transpose("janaki"))

'''
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
 but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''

def warm_up(x,y):
    if x % 2 ==0 and y % 2 ==0:
        if x>y :
            return y
        else:
            return x
    else:
        if x >y:
            return x
        else:
            return y

print(warm_up(2,4))
print(warm_up(2,5))

'''

ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
'''
def animal_crackers(word):
    w=word.split()
    if w[0][0] == w[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

'''
MAKES TWENTY: Given two integers, 
return True if the sum of the integers is 20 or if one of the integers is 20.
 If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
'''
def makes_twenty(x,y):
    if x+y== 20 or x== 20 or y == 20:
        return True
    else:
        return False

print()
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
'''
def mac_doanld(word):
    t=''
    for i,w in enumerate(word):
        if i ==0 or i == 3:
            t+=w.upper()
        else:
            t+=w
    print(word[:1].upper()+word[1:3]+word[3:4].upper()+word[4:])  # this also gives the same output 'MacDonald'
    return t

print(mac_doanld('macdonald'))

'''

MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
'''

def master_yoda(sentence):
    w=sentence.split()
    w.reverse()
    result = " ".join(w)
    return result


print(master_yoda("I am home"))
print(master_yoda("We are ready"))

'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''
def has_33(list):
    index=[i for i,v in enumerate(list) if v == 3]
    print(index)
    if index[1] - index[0] == 1:
        return True
    else:
        return False


print(has_33([1,3,3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

'''

PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiissssssiiippppppiii'
'''

def paper_doll(word):
    text=''
    for w in word:
        text+=w+''.join(w*2)
    return text


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


'''

BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
 If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
 Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

def black_jack(a,b,c):
    sum=a+b+c
    if sum <= 21:
        return sum
    elif sum> 21:
        if a ==11 or b ==11 or c ==11:
            sum-=10
            if sum >21:
                return 'Bust'
            else:
                return sum
        else:
            return 'Bust'

print(black_jack(5,6,7))
print(black_jack(9,9,9))
print(black_jack(9,9,11))

'''
SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers.¶
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''

def summer_69(mylist):
    indexlist=[i for i, v in enumerate(mylist) if v == 6]
    # print(len(indexlist))
    filterlist=[]
    if len(indexlist) == 0:
        filterlist = mylist[:]
    elif mylist[indexlist[0]] == 6 and mylist[indexlist[0]+1] == 9:
        filterlist=mylist[:indexlist[0]]+ mylist[indexlist[0]+2:]
    elif mylist[indexlist[0]] == 6:
        filterlist = mylist[:indexlist[0]]

    print(filterlist)
    return sum(filterlist)

print(f"\n {summer_69([1, 3, 5])}")
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

