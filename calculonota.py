# Dados de entrada (Notas do aluno)
nota1 = 9.2
nota2 = 6.8
nota3 = 7.5

# --- Cálculo da Média ---

# 1. Somar todas as notas
soma_notas = nota1 + nota2 + nota3

# 2. Definir o número de avaliações
numero_notas = 3

# 3. Calcular a média
media = soma_notas / numero_notas

# --- Exibição dos Resultados ---

print("--- Resultado da Média Escolar ---")
print(f"Notas registradas:")
print(f"  Prova 1: {nota1:.1f}")
print(f"  Prova 2: {nota2:.1f}")
print(f"  Prova 3: {nota3:.1f}")
print("-" * 30)

# Exibe o resultado final arredondado para duas casas decimais
print(f"A Soma das notas é: {soma_notas:.2f}")
print(f"A Média Final do aluno é: {media:.2f}")
