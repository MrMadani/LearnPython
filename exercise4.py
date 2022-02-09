#pattern printing
#input integer
#boolean varialbe will depend how the pattern will print
#
user_input=int(input("enter the number of rows you want to print "))
boolean_value = int(input("enter boolean value: "))

if boolean_value == 1:
    for i in range(1, user_input+1):
        print("*"*int(i))
elif boolean_value == 0:
    for i in range(user_input, 0, -1):
        print("*" * i)