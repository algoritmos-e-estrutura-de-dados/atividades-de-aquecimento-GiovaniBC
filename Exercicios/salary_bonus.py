nome = input("Informe seu nome: ")
sfix = input("Informe seu salário fixo: ")
dvenda = input("Informe o quanto faturou em suas vendas: ")

salary = float(sfix) + float(dvenda) * 0.15

print(f"TOTAL = R$ {salary}")