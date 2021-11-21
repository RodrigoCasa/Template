print("Bem-vindo à Pizzaria")

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

Pizza1 = Normal * 10.00

Pizza2 = Peppe * 12.00

Pizza3 = Vege * 10.00

Pizza4 = Mussa * 15.00

Pizza5 = Port * 15.00

Pizza6 = Itali * 12.00

Pizza7 = Broco * 12.00

Pizza8 = Água * 3.00

Pizza9 = Bebi * 5.00

Total = Pizza1 + Pizza2 + Pizza3 + Pizza4 + Pizza5 + Pizza6 + Pizza7

Bebida = Pizza8 + Pizza9

Quantidade = int(input("Escreva a quantidade de acompanhantes: "))

Idade = int(input("Há um menor de idade acompanhando? Se sim escreva quantos, se não há nenhum digite apenas 0: "))

if(Idade<=0):
    print("Certo")
elif(Idade>=1):
    print("Certo, um desconto será aplicado no valor final")

Desconto0 = 0.15 * Idade

Desconto1 = Desconto0 * 100

Desconto2 = (Total * Desconto1) / 100

Desconto3 = Total - Desconto2

for Tempo in range(1,16,1):
    print(f"Aguarde um pouco, estamos enviando o pedido para nossos cozinheiros: {Tempo}")

print(f"O preço total em pizza será: {Desconto3} Reais")
print(f"O preço total em bebidas será: {Bebida} Reais")

print("Pedido finalizado, aguarde o pedido em seus lugares")