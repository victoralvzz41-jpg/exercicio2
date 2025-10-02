# Dados de entrada
distancia_percorrida_km = 450.0  # Nova distância em km
combustivel_gasto_litros = 32.5  # Novo consumo em litros

# --- Cálculo do Consumo Médio (Km/l) ---

# Fórmula: Consumo Médio = Distância / Combustível Gasto
consumo_medio = distancia_percorrida_km / combustivel_gasto_litros

# --- Exibição dos Detalhes da Viagem ---

print("--- Relatório de Consumo de Combustível ---")
print(f"Distância Total Percorrida: {distancia_percorrida_km:.1f} km")
print(f"Combustível Gasto: {combustivel_gasto_litros:.2f} litros")
print("-" * 40)

# Exibe o resultado final, arredondado para duas casas decimais
print(f"Consumo Médio (Km/l): {consumo_medio:.2f} km/l")