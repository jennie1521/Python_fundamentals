# file input/output

#read
f=open("file.txt","r") #opens file
data=f.read() #read file
print(data)
line1=f.readline() #reads one line at a time
f.close() #always close file 

#write
f=open("file.txt","w") #opens file, if file not exist it will create file
data=f.write("my age is 21") #write into file, overwrites
f.close()

#read+ 
f=open("file.txt","r+") #overwrites from starting
data=f.write("abc") 
f.close()

#write+
f=open("file.txt","w+") #truncates the file 
# data=f.write("abc") 
data=f.read()
print(data)
f.close()

#append
f=open("file.txt","a") #appends data at last of the file 
# data=f.write("abc") 
data=f.read()
print(data)
f.close()

#with syntax
with open("file.txt","a") as f:
    data=f.read()
    #no need to close if using 'with' syntax 

#delete file
import os
os.remove("file.txt")

#write in file
with open("Practice.txt","w") as f:
    f.write("Hi\nmy name is janvi.\n")
    f.write("my age is 21")
