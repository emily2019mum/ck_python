"""
编写一个简单的Python程序，实现一个简易的计算器。
用户可以输入两个数字和一个运算符（+、-、*、/），程序将根据运算符执行相应的计算操作，并输出结果。
"""

def calc_op():
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    operator = input("请输入运算符（+、-、*、/）：")


    # 根据运算符执行相应的计算操作
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "除数不能为零"
    else:
        result = "无效运算符"


    # 输出计算结果
    print("计算结果：", result)

calc_op()