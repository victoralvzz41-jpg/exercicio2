# Dados de entrada
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# --- Cálculos ---
# Conversão para Dólar: valor em reais / taxa do dólar
valor_dolar = valor_reais / taxa_dolar

# Conversão para Euro: valor em reais / taxa do euro
valor_euro = valor_reais / taxa_euro

# --- Exibição dos Resultados ---
print(f"--- Conversor de Moedas ---")
print(f"Valor a ser convertido: R$ {valor_reais:.2f}\n")

# Exibe o valor em Dólar, arredondando para 2 casas decimais
print(f"R$ {valor_reais:.2f} equivalem a: $ {valor_dolar:.2f} (Dólar)")

# Exibe o valor em Euro, arredondando para 2 casas decimais
print(f"R$ {valor_reais:.2f} equivalem a: € {valor_euro:.2f} (Euro)")
