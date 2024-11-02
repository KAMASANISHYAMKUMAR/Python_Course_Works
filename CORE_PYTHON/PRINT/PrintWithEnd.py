
x=10         #int
y=12.12   #float
z='SssiT'  #str

print(x) #10
print(y) #12.12
print(z) #SssiT

''' print( ) will print the result on  the screen and
it will throw the cursor to next line, Reason
by default end attribute value of print( ) is \n

            Syn: print(value,value,......,sep=' ')
            Syn: print(value,value,.....,end='\n')
            
           printf( ) + "\n" ==> print()
           printf("welcome \n") ===> print("welcome")
'''

print(x,end='\n')
print(y,end='\n')
print(z,end='\n')
print("==========")

print(x,end='') 
print(y,end='\n') #1012.12
print(z) #1012.12SssiT
print("Shashi")

'''Note : based on the application req we can use
both sep and end attribute in print( ) at a time
           print(value,value,....,sep=' ',end='\n')
           print(value,value,....,end='\n',sep=' ')
'''








