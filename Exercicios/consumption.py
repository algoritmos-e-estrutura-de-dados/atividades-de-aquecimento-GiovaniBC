x = input("Insira a distância viajada do carro: ")
y = input("Insira o total de combustível gasto: ")

kml = int(x) / float(y)

print(F"{kml: .3f} km/l")