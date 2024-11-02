
f=open("data4.txt","w")

lst=["1.Have a nice day \n",
        "2.Have a Good Day \n",
        "3.Happy to see U ...."]

f.writelines(lst)

f.close()
print("Data is Saved ")
