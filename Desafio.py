import sys

def solve():
    input_line = sys.stdin.readline
    
    # 1. Leitura das 5 pontuações
    pontos = [int(input_line()) for _ in range(5)]
    
    # 2. Cálculo da média
    media = sum(pontos) / len(pontos)
    
    # 3. Lista e contagem dos elementos acima da média
    acima_da_media = [p for p in pontos if p > media]
    qtd_acima = len(acima_da_media)
    
    # Exibição das saídas
    print(f"Pontuações: {pontos}")
    print(f"Média: {media}")
    print(f"Acima da média: {acima_da_media}")
    print(f"Quantidade acima da média: {qtd_acima}")

if __name__ == '__main__':
    solve()