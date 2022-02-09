# def funtion_name_print(a,b,c,d):
#     print(a,b,c,d)

#for multiple input we need to use multible paramer
#to handlel this we use *args and **kwargs
#her *arg take a tuple  as an argument where **kwargs takes a Dictionary as an argument
# def sum(*args):
#     print(type(args))
#     sum=0
#     for i in args:
#         sum += int(i)
#
#     return sum
# limit= int(input("enter the how many numbers you want to add: "))
#taking user input in a list
# lstsum = []
# for x in range(0,limit):
#     user_input = int(input("enter the numbers you want to add: "))
#     lstsum.append(user_input)
#
# print(sum(*lstsum))


# a, b, c = '1 1 1'.split()
# print(a,b,c)
# a = "hello what is your date of birth"
# b= a.split()
# print(b)
# print(b[2])
#
# a,s,d,f = [1,2,3,4]
# print(a,s,d,f)

#using kwargs
def passingKeys(a,b,c):
    print(v,b,c)#here the key should be matched to output.
def passingKeyValues(**a):
    for i , j in a.items():
        print(i,j)

a={'a': "shahin", 'b':"shaker", 'c':"akib"}
# passingKeys(**a)
passingKeyValues(**a)