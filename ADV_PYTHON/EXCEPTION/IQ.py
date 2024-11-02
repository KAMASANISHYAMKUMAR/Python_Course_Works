'''
1.try: pass   //invalid 
2.except : pass  //invalid 
3.else: pass  //invalid 
4.finally: pass //invalid
'''

#1
try:   pass
except : pass

#2
try: pass
except : pass
else: pass

#3
try: pass
except : pass
finally : pass

#4
try: pass
finally: pass

#5
try: pass
except : pass
else: pass
finally: pass

'''Note: we can write any of the above forms in the
try or except  or else or finally  '''

try:
   try: pass
   except ValueError: pass
except:
    pass
else:
    pass
finally:
    pass



















