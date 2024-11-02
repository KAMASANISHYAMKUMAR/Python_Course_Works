#mydbmodule.py

import cx_Oracle
import time

def deleteRec(no):
    conn=cur=None
    try:
        conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

    except cx_Oracle.DatabaseError as e:
        print("Sorry Unable to continue....")
        print("Reason : ",e)

    else:
        print("connection is Est")
        cur=conn.cursor()
        print("cursor object is Created ")

        cur.execute("delete from emp where empno=%d" %no)
        print(cur.rowcount," Rec are deleted....")
        conn.commit()

    finally:
        if cur!=None:
            cur.close()

        if conn!=None:
            conn.close()
