
Install Python 3.6 higher version
Install Oracle 11.2 and higher version
Install cx_Oracle module
    -> Open the command prompt
    -> pip install cx_Oracle
              | Make sure u r system should be
                              connected with network

Steps For PDBC:
====================
Step-1
import cx_Oracle
     if req any other modules.

Step-2
  Est the connection with Oracle Database
   by using connect() from cx_Oracle
           connect(str,str,str) -> connection class object

    str : username of Database | scott
    str : password of Database user | tiger
    str : DB information
            Location of DB : portnumber / serviceId
            localhost: 1521 / orcl5
            IP Address

Port Number:
    - Every database will have unique port number
    - Default port number for oracle is 1521 | fixed

Service ID:
    - Every Data base will also have unique service ID
    - Service ids are not fixed
    - Default ServiceID of Oracle DB is Orcl

In Oracle:
    SQL>select * from global_name;
    ORCL5




import cx_Oracle

conn=cx_Oracle.connect("scott","tiger",
                            "localhost:1521/orcl5")

if conn!=None:
    print("connection is Est ")
else:
    print("connection is Fail")

    
Step-3: Create cursor class object For sending
queries to the Database

   > To create cursor class object then we have to
   use cursor( ) from connection it will return cursor
   object.

   cur=conn.cursor()
   print("Cursor object is Created ")


Step-4: Use the cursor class object For sending
Queries to execute @ Database.

     by using execute(str) from cursor class.
             cur.execute(str)
                str rep : Oracle Command
                Create | Insert | update | Delete | select...

Note: After Executing Insert | update | delete
commands then we have to call commit() from
connection class other wise those changes are
not effected to the database.

2.After Executing Any Select Statement then
Result of the Select Statement will be stored
in the same cursor object,

              If u get the Records from the cursor object
              then we have to use following methods
              from cursor class.
                  fetchone() -> tuple 
                  fetchmany() --> list of tuples 
                  fetchall() --> list of tuples

Step-5: Close the cursor object and Connection
object as well
        cur.close()
        conn.close()




        
    
 






    
    


    
                







    






















    
