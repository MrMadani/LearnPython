"""
in an open function there are these modes which we can pass as parameters.
"r" - open file for reading
"w" - Open a file for writhing
"x" - creates file if not exists
"a" - Add more content to a file
"t" - text mode
"b"- binary mode
"+" - read and write
"""
#in open function
f = open("text.txt","r")
# content = f.read()
# print(type(content))
# print(content)
# f.close()
# we cant read the file
# so to read the file we have to use the read funtion of the file class;
print(f.read())
# f.close()
#after opening a file the file must be closed
#it is a very good pratice
f = open("text.txt")

print((str(f.readlines())).find("is"))  #will give which index number of a particular search
#used a string method.find()

f.close()

