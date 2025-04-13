def maior(a, b):
    return (a + b + abs(a - b)) // 2


# Leitura dos três valores inteiros
a, b, c = map(int, input().split())

# Calcula o maior entre a e b, depois compara com c
maior_ab = maior(a, b)
maior_abc = maior(maior_ab, c)

# Exibe o resultado final
print(f"{maior_abc} eh o maior")
