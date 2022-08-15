def arithmetic(x, y, oper):
    """simple calculator to do four operations
    (concatenation, substraction, division, multiplication)"""
    if oper == "+": 
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "/":
        return x / y
    elif oper == "*":
        return x * y
    else:
        print("Invalid operation")

print("input first number")
x = float(input())
print("input second number")
y = float(input())
print("choose operation")
oper = input()
print(arithmetic(x, y, oper))
