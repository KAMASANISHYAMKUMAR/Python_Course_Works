
import cx_Oracle

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry unable to continue....")
    print("Reason : \n",e)

else:
    print("Connection is est ")
    cur=conn.cursor()
    print("cursor object is created ")

    query="SELECT ENAME,JOB,SAL FROM EMP"
    cur.execute(query)
    t=cur.fetchone()
    print("Rec is : ",t)          

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()


        

