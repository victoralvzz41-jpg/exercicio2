# Dados de entrada
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20  # Representa 20%

# --- Cálculos ---

# 1. Converter a porcentagem para um valor decimal
taxa_desconto = porcentagem_desconto / 100  # 20 / 100 = 0.20

# 2. Calcular o valor exato do desconto
valor_desconto = preco_original * taxa_desconto

# 3. Calcular o preço final
preco_final = preco_original - valor_desconto

# --- Exibição dos Detalhes ---

print(f"--- Detalhes do Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto Aplicado: {porcentagem_desconto}%")

print(f"\nValor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")