# file IO Basic
"""
"r" - open file for readin g
"w" - Open a file for writhing
"x" - creates file if not exists
"a" - Add more content to a file
"t" - text mode
"b"- binary mode
"+" - read and write
"""
"""
#file reading
# f.close()
#after opening a file the file must be closed
#it is a very good pratice
f = open("text.txt")

print((str(f.readlines())).find("is"))  #will give which index number of a particular search 
#used a string method.find()

f.close()

"""
"""
#file .tell() .seek() methods
f = open("text.txt") #used to open a file and point it to f
print(f.readline()) #used to print a line in a file
print(f.tell()) #it tells where the file pointer  lies
print(f.seek(2)) #it reset the file pointer to any index i like.
print(f.read())  # used to read the whole file starting from where the starting index points.
f.close()
"""
#opening files using with blocks.
f = open("text.txt")
print("for f ",f.readline())
f.close()

with open("text.txt") as f:
    a = f.read(4)  #anything inside the brackets specifies how many character will be stored in str a
    b = f.readlines()
    print("for b: ",b)
    print(type(a))
    #after open with file the file automaticaly calls the close() method.
z=open("text.txt")
print("for z" , z.read())