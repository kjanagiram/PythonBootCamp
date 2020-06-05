print('Conditional IfStatements')

hungry=True

if hungry:
    print("Yes, I am Hungry")
else:
    print("No, I am not Hungry")

number =17

if number%2 ==0:
    print(f"{number} is even")
else:
    print(f"\n{number} is odd")

no1=5
no2=3
no3=9
if no1>no2:
    print(f"\n{no1} is greater than {no2}")
else:
    print(f"\n{no1} is less than {no2}")


if  no1 > no2 and no1 >no3:
    print(f"\n{no1} is greater than the {no2} and {no3}")
elif no2>no1 and no2>no3:
    print(f"\n{no2} is greater than the {no1} and {no3}")
else:
    print(f"\n{no3} is greater than the {no1} and {no2}")

n=1
if n%5==0:
    if n%11==0:
        print(f"{n} is divisible by 5 and 11")
    else:
        print(f"{n} is divisble by 5, but not by 11")
else:
    print(f"{n} is not divisible by 5 and 11")
ch='b'
print(ord(ch))

if ord(ch)>64 and ord(ch)<91:
    print(f"{ch} is uppercase")
elif ord(ch) >96 and ord(ch)<123:
    print(f"{ch} is lowercase")
else:
    print(f"{ch} is number")
