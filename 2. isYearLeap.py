def isYearLeap(year):
	if year % 4 == 0:
		print("Этот год високосный")
	else:
		print("Этот год не високосный")
		
year = int(input("Введите год: "))
isYearLeap(year)