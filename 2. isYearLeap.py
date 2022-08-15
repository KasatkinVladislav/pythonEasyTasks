def isYearLeap(year):
        """this function can define, is inputted year leap or common"""
	if year % 4 == 0:
		print("this year is leap")
	else:
		print("this year is common")
		
year = int(input("input year: "))
isYearLeap(year)
