print("Bem-vindo à Pizzaria")

Quantidade = int(input("Escreva a quantidade de acompanhantes: "))

print("Vamos passar nosso cardápio, digite a quantidade do pedido em números, se não desejar nada digite apenas 0 ")

Normal = int(input("1-Pizza Tradicional: "))

Peppe = int(input("2-Pizza de pepperoni: "))

Vege = int(input("3-Pizza Vegetarina: "))

Mussa = int(input("4-Pizza de Mussarela: "))

Port = int(input("5-Pizza Portuguesa: "))

Itali = int(input("6-Pizza Italiana: "))

Broco = int(input("7-Pizza de Brócolis: "))

Água = int(input("8-Água: "))

Bebi = int(input("9-Bebida: "))

Pizza1 = Normal * 10

Pizza2 = Peppe * 12

Pizza3 = Vege * 10

Pizza4 = Mussa * 15

Pizza5 = Port * 15

Pizza6 = Itali * 12

Pizza7 = Broco * 12

Pizza8 = Água * 3

Pizza9 = Bebi * 5

Total = Pizza1 + Pizza2 + Pizza3 + Pizza4 + Pizza5 + Pizza6 + Pizza7

Bebida = Pizza8 + Pizza9

print(f"O preço total em pizza será: {Total} Reais")
print(f"O preço total em bebidas será: {Bebida} Reais")

