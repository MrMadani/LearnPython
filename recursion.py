def Iteratinvefactorial(n):
    """
    :param n: interger
    :return: n * n-1 * n-2* n-3
    """
    for i in range(n):
        fac = fac * (i+1)
    return fac
def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
def fibonaci(n):
    # total = 0
    # for i in range(n):
    #     total = total +(total + total)
    # return total
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
numbers = int(input("enter number : "))
print(fibonaci(numbers))

print(range(4))


