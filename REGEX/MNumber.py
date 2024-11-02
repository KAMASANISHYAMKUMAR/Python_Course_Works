
For Regular Expression
   re module

import re

1.What to Search | Pattern
        - we can specify the pattern by using
                  compile(str) -> pattern class object
                  p=re.compile("m\w\w")
                            \w means any A|N character
                            
2.Where to Search | Target
        - We can specify the target by using following
        methods from pattern class.
             match( ) -> Match object | None 
             search( ) -> Match object | None 
             findall( ) --> list

             finditer(pattern,target) -> callable_iterator
               callable_iterator is the collection of
                                                        Match objects

              fullmatch(pattern,target) -> Match | None

              split(pattern,target ) -> list
              sub(pattern,replacementstr,targe) -> str
              subn(pattern,replcementstr,target) -> tuple
              
              

import re

p=re.compile("m\w\w")
m=p.match("dad mam man map run gun mad")
                                        or
m=re.match("m\w\w","dad mam man map run gun mad")
print("==================================")

p=re.compile("m\w\w")
m=p.search("dad mam man map run gun mad")
                                 or
m=re.search("m\w\w","dad mam man map run gun mad")
print("====================================")

p=re.compile("m\w\w")
lst=p.findall("dad mam man map run gun mad")
                                    or
lst=re.findall("m\w\w","dad mam man map run gun mad")


Match Object :
    span
       - starting index pos of match
                      start( ) -> int
                      
       - ending index+1 pos of the match
                      end( ) -> int  

    match
       - Matched String
           to get Matched string use group() -> str 

Application-1:
==========================
Pattern For validating Mobile Number
    1.It should allow only digits
    2.Total number of digits should be 10
    3.Number should be start 6 | 7 | 8 | 9

[6789][0-9][0-9][0-9]
            [0-9][0-9][0-9]
            [0-9][0-9][0-9]   //valid

[6-9][0-9]+   // Wrong
         [0-9]+ means any digit any no.of.times

[6-9][0-9]*   //Wrong
     [0-9]* Means any digit for 0-times or Any no.of.times

[6-9][0-9]{9}
         [0-9]{9}  means any digit For 9 times
        or 
[6-9]\d{9}

==================================
Pattern For validating Mobile Number
    1.It should allow only digits
    2.Total number of digits should be 10 or 11
    3.Number should be start 6 | 7 | 8 | 9
    4.If it is 11 digits then it should be start with 0

  [6-9][0-9]{9}   --> 10 digits
  0[6-9][0-9]{9}   --> 11 digits

  0?[6-9][0-9]{9}
     0?   --> 0 For 1-Time or 0 For 0-times

===========================================
Pattern For validating Mobile Number
    1.It should allow only digits
    2.Total number of digits should be 10 or 11 or 12
    3.Number should be start 6 | 7 | 8 | 9
    4.If it is 11 digits then it should be start with 0
    5.If it is 12 digits then starts with 91

[6-9][0-9]{9}   --  10
0[6-9][0-9]{9}  -- 11
91[6-9][0-9]{9} -- 12


91?0?[6-9][0-9]{9}   // Invalid
  91?  91-For 1 or 0-time
     0?  0-For 1 time or 0-time

91089999999999

(91|0)?[6-9][0-9]{9}
   (91|0) ? means    either 91 or 0 for 1-time or 0-times

======================================
Pattern For gmail-ID
|  |----------2--------|    |---- 3 -------|
s hashikumar.ch @ gmail.com

[a-zA-Z0-9]
[a-zA-Z0-9_.]+
@
gmail[.]com
==================================

|  |----------2--------|    |---- 3 -------|
s hashikumar.ch @ gmail.com
                                     yahoo.com
                                     v6.net
                                     tv9.com

[a-zA-Z0-9]
[a-zA-Z0-9._]+
@
[a-z0-9]+[.][a-z]+
=====================================
|  |----------2--------|    |---- 3 -------|
s hashikumar.ch @ gmail.com
                                     yahoo.com
                                     v6.net
                                     tv9.com
                                     ts.gov.in
                                     uk.edu
                                     uk.online.edu
[a-zA-Z0-9][A-Za-z0-9._]+@[a-z0-9]+ [ [.][a-z]+ ]+
    
















                                     




































   








  














    






     

  
  














     






            
    




             
             








