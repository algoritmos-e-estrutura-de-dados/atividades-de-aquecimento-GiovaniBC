var = input()
a, b, c = var.split(' ')

maiorAB = (int(a) + int(b) + abs (int(a) - int(b))) / 2
maiorABC = (maiorAB + int(c) + abs (maiorAB - int(c))) / 2

print(F"{maiorABC} eh o maior")