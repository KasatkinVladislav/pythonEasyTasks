def bankDeposit(amountMoney, years):
    """this function calculates sum of money on a bank deposit"""
    sum = amountMoney
    for oneYear in range(years):
        sum = sum * 1.1
    return sum

print("input amount of money")
amountMoney = float(input())
print("input count of years")
years = int(input())
print(bankDeposit(amountMoney, years))
