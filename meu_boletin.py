notas = []

for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

print("Lista de notas:", notas)
print("Soma:", sum(notas))
print("Média:", sum(notas) / 4)