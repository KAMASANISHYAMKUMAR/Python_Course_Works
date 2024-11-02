
'''
To Extract Input From the user We
have to use the following function

C-Language :   scanf( )
C++ : cin
Java: Scanner
Python: input( ) vs raw_input( ) 2.x version
'''

int sum(int x,int y)
{
    int s;
    s=x+y;
    return s;
}

int sum(int,int);   ------>    sum(x,y) -> int 
int s=sum(10,20);              s=sum(10,20)
                                               type(s)   #<class 'int'>

float sum(int,int,int);  --->  sum(x,y,z) -> float 
float r=sum(10,20,30);       r=sum(10,20,30)
                                                 type(s) #<class 'float'>
                                                 
void sum(int,int);    ---->      sum(x,y) -> None
sum(10,20);                           sum(10,20)

=========================================
sum(x,y[,z]) -> int
r=sum(10,20,30)
r=sum(10,20)
type(r)  #<class 'int'>

sum(x[,y,z]) -> float
r=sum(10)
r=sum(10,20,30)
===============================

sum(x,y,z=90) ->  float
r=sum(10,20)
r=sum(10,20,30)














































