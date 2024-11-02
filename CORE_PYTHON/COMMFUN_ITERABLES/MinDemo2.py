import time

#len(iterable) -> value
#sum(iterable) -> value
#min(iterable) -> value

s="welcome"
print("string : ",s)

small=ord( s[0] )

for i in s:
    time.sleep(.2)
    print(ord(i),"--->",i)
    if ord(i)<small:
        small=ord(i)

print("=====================")
print("Smallest : ",chr( small ) )

print("Smallest char : ", min(s) )










