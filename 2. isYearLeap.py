def isYearLeap(year): #this function can define, is inputted year leap or common
	if year % 4 == 0:
		print("Этот год високосный")
	else:
		print("Этот год не високосный")
		
year = int(input("Введите год: "))
isYearLeap(year)