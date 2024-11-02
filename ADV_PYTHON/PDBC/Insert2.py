
import cx_Oracle

conn=None
cur=None




try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl5")

except cx_Oracle.DatabaseError as e:
    print("Sorry Unable to continue...")
    print("Reason : \n",e)

else:
    print("Connection is Est ")
    cur=conn.cursor()
    print("Cursor object is Created ")

    query="INSERT INTO STINFO VALUES(%d,'%s','%s')"

    while True:
        sno=int( input("Enter sno : ") )
        sname=input("Enter sname : ")
        scity = input("Enter scity : ")
    
        cur.execute(query %(sno,sname,scity))
        conn.commit()        
        opt=input("Do u want another rec y | n ")
        print("=============================")

        if opt in['N','n']:
            break
        
        print("Rec is Inserted ")

finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()


        


        
