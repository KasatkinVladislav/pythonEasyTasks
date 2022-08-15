def square(a):
        """this function counts a perimeter, space and
        diameter of a square based on a side of it"""
	p = a * 4 #perimeter
	s = a * a #space
	d = (s + s) ** (0.5) #diameter
	return (p, s, d)
	
a = int(input("input side of a sqare "))
print(square(a))
