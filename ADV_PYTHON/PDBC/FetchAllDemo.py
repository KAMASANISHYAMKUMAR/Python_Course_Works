
import cx_Oracle
import time

conn=cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as r:
    print("Sorry Unable to continue...")
    print("Reason : \n",r)

else:
    print("Conenction is Est ")
    cur=conn.cursor()
    print("Cursor object is Created ")
    
    cur.execute("SELECT * FROM DEPT")

    #lt=cur.fetchall()
    #for t in lt:

    for t in cur:
        time.sleep(1)
        print("Deptno : ",t[0])
        print("Dname is : ",t[1])
        print("Dloc is : ",t[2])
        print("=================")    

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()

        
