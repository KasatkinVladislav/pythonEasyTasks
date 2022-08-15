def seasons(x):
    """this function can tell which season it is based on a number of a month"""
    if x < 3 or x == 12: 
        return "it is winter"
    elif x < 6 and x > 2:
        return "it is spring"
    elif x < 9 and x > 5:
        return "it is summer"
    elif x < 12 and x > 8:
        return "it is autumn"
    else:
        return "this is not a number of a month"

print("input number of a month")
x = int(input())
print(seasons(x))
