

f=input("Enter First String : ")
s=input("Enter Second String : ")

if len(f)==len(s):
    if f>s:
        print("Biggest string : ",f)
    elif s>f:
        print("Biggest String : ",s)
    else:
        print("Both String are same")
else:
    print("sorry string are not in same length ")
