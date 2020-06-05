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