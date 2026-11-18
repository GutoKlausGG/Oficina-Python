numeros = []
pares = []

quantidade = int(input("Quantos números você vai digitar? "))

for i in range(quantidade):
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)

print("Números digitados:", numeros)
print("Números pares:", pares)
print("Quantidade de pares:", len(pares))