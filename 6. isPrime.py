def isPrime(number):
    """this function can tell is the number prime"""
    if number == 1:
        return "this number is prime"
    isPrimeBool = True
    for i in range(2, number):
        if (number % i) == 0:
            isPrimeBool = False
    if isPrimeBool:
        return "this number is prime"
    else:
        return "this number is not prime"

print("input number")
number = int(input())
print(isPrime(number))
