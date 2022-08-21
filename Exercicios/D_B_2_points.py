p1 = input()
x1, y1 = p1.split(' ')
p2 = input()
x2, y2 = p2.split(' ')

dist = ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)**0.5

print(F"{dist: .4f}")