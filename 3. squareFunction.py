def square(a):
	p = a * 4 #perimeter
	s = a * a #space
	d = (s + s) ** (0.5) #diameter
	return (p, s, d)
	
a = int(input("введи сторону квадрата "))
print(square(a))