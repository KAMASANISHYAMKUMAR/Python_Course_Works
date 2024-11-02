
import cx_Oracle

conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

if conn!=None:
    print("Connect is Est ")

    cur=conn.cursor()
    print("Cursor object is Created ")

    query="CREATE TABLE STINFO(SNO NUMBER(3),SNAME VARCHAR(10),SCITY VARCHAR(10))"  
    cur.execute(query)
    print("Table is Created ....!!!")

    cur.close()
    conn.close()
    
else:
    print("connection is Fail")

