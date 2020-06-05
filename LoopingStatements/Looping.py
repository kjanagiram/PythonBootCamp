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