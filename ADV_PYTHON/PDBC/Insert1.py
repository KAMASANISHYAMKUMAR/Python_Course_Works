import cx_Oracle
cur=None
conn=None
try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry Unable to continue....")
    print("Reason : ",e)

else:
    print("Connection is est ")
    
    cur=conn.cursor()
    print("Cursor object is created ")
    query="INSERT INTO STINFO VALUES(101,'JAI','HYD') "
    cur.execute(query)
    conn.commit()
   
    print("Rec is inserted ")

finally:
    if cur!=None:
        cur.close()

    if conn!=None:    
        conn.close()
    
    




    








    








