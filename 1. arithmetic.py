def arithmetic(x, y, oper): #simple calculator to do four operations (concatenation, substraction, division, multiplication)
    if oper == "+": 
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "/":
        return x / y
    elif oper == "*":
        return x * y
    else:
        print("Твой опер какой-то не такой")

print("Введи х")
x = float(input())
print("Введи у")
y = float(input())
print("Выбери операцию")
oper = input()
print(arithmetic(x, y, oper))
