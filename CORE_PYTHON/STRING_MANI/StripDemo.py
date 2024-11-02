
#S.lstrip([chars]) -> str
''' it will return new string object after
erasing specified chars from the left side
of string object. If we fail to specify the chars
to trim then it will erase empty spaces if exists '''

s1="xysssit"
print("Data is : ",s1)

s1=s1.lstrip('xy')
print("Result is : ",s1)
print("====================")

#S.rstrip([chars]) -> str
s3="sssitxy"
print("Data is : ",s3)

s3=s3.rstrip("xy")
print("Result is : ",s3)
print("====================")

#S.strip([chars]) -> str
s="    sssit     "
print("Data is : ",s)

s=s.strip()
print("Result is : (%s) " %s)

























