#exercise - faulty
result=0
i = 0
while i != 1:
    try:
        opr = input("enter your operator: ")
        user_input1 = int(input("enter your first number: "))
        user_input2 = int(input("enter your second number: "))
        if user_input1 == 45 and user_input2 == 3 and opr == '*':
            print("your result is 555")
        elif user_input1 == 56 and user_input2 == 9 and opr == '+':
            print("your result is 77")
        elif user_input1 == 56 and user_input2 == 6 and opr == '/':
            print("your result is 4")
        else:
            if opr == '+':
                result = user_input1 + user_input2
            elif opr == '-':
                if user_input1 > user_input2:
                    result: user_input1 - user_input2
                else:
                    result = user_input2 - user_input1
            elif opr == '/':
                result = user_input1 / user_input2
            elif opr == '*':
                result = user_input1 * user_input2
    except Exception as e:
        print(e)
    finally:
        if result != 0:
            print(f"the result is {result}")
        i = int(input("enter 1 to stop and 2 to continue"))








