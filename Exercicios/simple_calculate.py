produto1 = input("Insira, respectivamente e espaçadamente, o codigo, quantidade e preço unitario do primeiro produto: ")
cod1 , numUn1, precoUn1 = produto1.split(' ')

produto2 = input("Insira, respectivamente e espaçadamente, o codigo, quantidade e preço unitario do segundo produto: ")
cod2 , numUn2, precoUn2 = produto2.split(' ')

valor = int(numUn1) * float(precoUn1) + int(numUn2) * float(precoUn2)

print(f"VALOR A PAGAR = R$ {valor: .2f}")