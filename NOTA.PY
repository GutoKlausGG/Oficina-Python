alunos = int(input())
soma = 0
for i in range(alunos):
    nota = float(input())
    soma = soma + nota
media = soma / alunos
print(f"{media:.f}")