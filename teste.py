

# Lê os dados de entrada para peça 1
codigo1, numero_pecas1, valor_unitario1 = map(float, input().split())

# Lê os dados de entrada para peça 2
codigo2, numero_pecas2, valor_unitario2 = map(float, input().split())

# Calcula o valor total a ser pago
total_pecas1 = numero_pecas1 * valor_unitario1
total_pecas2 = numero_pecas2 * valor_unitario2
valor_total = total_pecas1 + total_pecas2

# Imprime o resultado conforme o formato esperado
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")