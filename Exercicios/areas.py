var = input("Insira 3 váriaveis espaçadamente: ")
pi = 3.14159

a, b, c = var.split(' ')

tri = float(a) * float(c) / 2
cir = float(c)**2 * pi
tra = (float(a) + float(b)) * float(c) / 2
qua = float(b)**2 
ret = float(a) * float(b)

print(F"TRINAGULO = {tri: .3f}")
print(F"CIRCULO = {cir: .3f}")
print(F"TRAPEZIO = {tra: .3f}")
print(F"QUADRADO = {qua: .3f}")
print(F"RETANGULO = {ret: .3f}")