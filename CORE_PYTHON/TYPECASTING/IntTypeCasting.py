
#int type casting using int( )
#float -> int
x=12.1212
y=int(x)
print(type(x)," ----> ", type(y) )
print("x : ",x," ----> ","y : ",y)
print("=====================")

#complex -> int
x=(10+20j)
''' y=int(x)
TypeError: int() argument must be a string, a bytes-like object or a real number,
not 'complex' '''

#str -> int
x="1223"
y=int(x)
print(type(x)," ----> ", type(y) )
print("x : ",x," ----> ","y : ",y)
print("=====================")
'''Note : ValueError: invalid literal for int() with base 10: '12.23 '''

#bool -> int   True - 1 | False - 0
x=False
y=int(x)
print(type(x)," ----> ", type(y) )
print("x : ",x," ----> ","y : ",y)
print("=====================")

































