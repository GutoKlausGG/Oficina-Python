n = int(input("Quantas notas?"))
notas = []
for i in range(n):
    notas.appemd(float(input("Nota: ")))
    print("Média:", sum(notas) / n, ".MAior:", max(notas))