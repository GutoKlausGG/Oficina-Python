n = int(input())
soma = 0

for _ in range(n):
    nota = float(input())
    soma += nota

media = soma / n
print(media)