
import cx_Oracle

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry unable to continue.....")
    print("Reason is \n ",e)

else:
    print("Connection is Est ")
    
    cur=conn.cursor()
    print("Cursor object is Created ")

    query="UPDATE EMP SET SAL=SAL+%d, COMM=COMM+%d where job='%s'"

    sal=int(input("Enter Increment Salary : "))
    com=int(input("Enter Increment comm : "))
    jobt=input("Enter job title : ")
    
    cur.execute(query %(sal,com,jobt))
    conn.commit()
    print(cur.rowcount," Rec are updated....")

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()

        
