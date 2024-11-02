


Types of Formal parameter
   - Positional arguments
        - By Default all formal parameters
          are positional arguments
        - In this case order and count of parameter
          must be maintained.          
        
   - Keyword arguments
        - By Default all formal parameters are also
        acts keyword arguments.

        - In this case order is not required to maintain
        but count of parameters required to maintain.

         - in this case we have to pass the values by
         using their names.

       
   - Positional only arguments
        - The Parameters which are declared
        left side of / parameter called positional only
        arguments

        - In this case order and count mut be maintained.
        - We have to pass the values to the parameter
           w.r.t their position.        
        
   - Keyword only arguments
         - The parameters which are declare
         right side of * parameter

              def myFun(*,x):
                  pass

          - order is not req to maintained.but count is
          req to maintain.

             
   - Default arguments
         - Process of defining the formal parameter
         with some values
         - Default parameters are acts as optional
         parameter
         - Default parameters are replaced by the
         actual arguments.
         
   - Varargs
          - The parameters which are declared with *

          def myFun(*,x,y):   #keyword argu
              pass

          def myFun(*x):  #*x varargs parameter
              pass

       - Varargs parameter can take 0 to N. no.of.
                              positional only arg
                              
       - But internally Varargs acts as tuple
       
           
   - kwargs arguments
       The parameter which are declared with in the
       function with **
                def myFun(*,x):
                   pass
                
                def myFun(*x):
                    pass

                def myFun(**x):
                    pass

      - kwargs parameter can take 0 to N no.of.keyword
         only arguments

      - kwargs internally works as dict collection
      





      





                
       






