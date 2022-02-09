#loops in python
# list1= ["harry","larry","carry", "marri"]
# for item in list1:
#     print(item, end=',')

list2= [["harry",1] , "shahin", {231:"name", 221:"fahim ", 223:"haddi"} , (1,2,4,5) ]

for item in list2:
    print(item)

print(str(list2[3][3]).isnumeric())
# items= [ int, float, "shahin", 1,2,45,65,4,3,2,3]
# for item in items:
#     if str(item).isnumeric() and item >= 6:
#         print(item)
#
# str1= str(items)
# print(str1)
# print(str1.isnumeric())