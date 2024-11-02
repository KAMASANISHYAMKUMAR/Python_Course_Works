
Flat Files :
    The Files Which are created
    either by using notepad or wordpad

    In The Flat files there is no support for tables.
    thus data can't be stored in the form of tables.

    Here we can store the data in the tabular format
    by , sep thus these files are called comma sep
    values CSV

    These files must be saved with .csv extension
              .py | .c | .cpp | .java | .csv

    These Files can be opened and edit in the excel
    as well

   Steps To Write the Data into CSV Files :
========================================

 1.Open the file in write mode
      f=open("data.csv","w")

 2.Create CSV writer class object by using
       writer(file) -> writer class object
       from csv module.

                     import csv
                     wo=csv.writer(f)
                     
3.to write the data into the csv file then we have to
use writerow(iterable) from writer class

                           lst=['sno','sname','scity']
                           wo.writerow(lst)

4.Close the file.
                   f.close()


STEPS For Reading the Data from CSV Files:
=======================================
1.open the file in read mode
    f=open("stu3.csv","r")

2.Create reader class object by using reader( )
from csv module
           reader(file) -> reader class object
             import csv
             ro=csv.reader(f)

3.Reader class object is holding all the records which
are existed in the csv file.
              Reader object is the list of list | iterable
              Each list is a record from csv File

4.close the file



              

















    







                     



       

















    
       
