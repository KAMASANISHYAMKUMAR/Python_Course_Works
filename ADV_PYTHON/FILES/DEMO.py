
  Based On the storage of the data
     Prgs are classified into 2 types
        1.Non persistency Prgs
        2.Persistency Prgs.
                  a.Using Files
                         
                  b.Using Databases
                              - Database basic ICURD


open( ) -> File class object | _io.TextIOWrapper 
   Syn: f=open("filename","filemode")

   File modes:
       "w" : write
           - write mode will open the file allow to write the
           data in the file.
           - If the specified file is already is existed then
           it will overwrite old with new data.

        "a" : append
           - append mode will open the file allow to write the
           data in the file.
           - If the specified file is already is existed then
           it will  add new Data to its previous.

         "r": read
            -  it is default mode
            - It will open the file and allow to read the data
            - If the specified file is not existed then
            it will raise FileNotFoundError

         "x" : Exclusive Mode
             - It will open the file and allow to write the data
             in the file iff the specified file is not existed
             - If the specified file is already existed then
             will raise an Error : FileExistsError

          "w+" : write + read
          "a+" : append + read

Properties
name
mode
closed

Methods
readable()
writable( )
close( )

For Writing:
    write(data)
    writelines(iterable)

For Reading :
    read( ) -> str
    read(bytes) -> str
    readline( ) -> str
    readlines( ) -> list







    








    











             
            







       
