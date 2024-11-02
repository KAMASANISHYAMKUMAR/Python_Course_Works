
import cx_Oracle
import time

conn=None
cur=None


try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry unable to continue....")
    print("Reason  is : \n ",e)

else:
    print("Connection is est")
    cur=conn.cursor()
    print("Cursor object is Created ")
    cur.execute("SELECT ename,job,sal from emp")
    lt=cur.fetchmany(5)

    for t in lt:
        time.sleep(1)
        for i in t:
            print(i,end='\t')
        print(" ")

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()
    
