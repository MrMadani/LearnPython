l = 10
#l is the global variable
def function(n):
    global l#this will help to change the value of l globally
    l=5
    #here l is local variable

    print(l+1)
function(5)
print(l)