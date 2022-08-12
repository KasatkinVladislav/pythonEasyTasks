def arithmetic(x, y, oper):
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
