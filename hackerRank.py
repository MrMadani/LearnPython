

# write your code here
# def avg(*num):
#     sum = 0
#     for i in num:
#         sum += int(i)
#     result = sum / 2
# type(*num)
#     return result
# print(avg("2",'5'))

def transformSentence(sentence):
    words=sentence.split()
    res = ""
    for i in words:#what =i
        res += i[0]#res =res + i ; i[0] = w
        for j in range(1, len(i)):
            if i[j-1].lower() < i[j].lower():
                res += i[j].upper()
            elif i[j-1].lower() > i[j].lower():
                res += i[j].lower()
            else:
                res += i[j]
        res += " "
    return res[:-1:]
userinput= str(input("enter "))
print(userinput.split())
# print(transformSentence(userinput))
