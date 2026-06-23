# ==============================================================================
# CONSTANTES (Convenção PEP 8: Letras Maiúsculas)
# ==============================================================================
# Valor de referência sugerido para gastos diários básicos em viagens internacionais
VALOR_MINIMO_DIARIO_USD = 50.0  
NOME_SISTEMA = "VAI VIAJAR? - SIMULADOR DE CUSTOS"

# ==============================================================================
# FUNÇÕES DE ENTRADA (Saída de boas-vindas e Captura de Dados)
# ==============================================================================
print(f"=== {NOME_SISTEMA} ===")
print("Preencha os dados abaixo para calcular a viabilidade do seu orçamento.\n")

# Todo input() captura os dados estritamente como o Tipo de Dado: String (Texto)
destino = input("Qual o destino da viagem? ")
dias_texto = input("Quantos dias você vai ficar lá? ")
reais_texto = input("Qual o seu orçamento total em Reais (R$)? ")
cotacao_texto = input("Qual a cotação atual do Dólar (ex: 5.25)? ")

# ==============================================================================
# CONVERSÃO DE TIPOS (Casting)
# ==============================================================================
# Para realizar cálculos matemáticos, convertemos as strings para números:
quant_dias = int(dias_texto)          # Tipo: Inteiro (int)
orcamento_reais = float(reais_texto)  # Tipo: Ponto Flutuante (float)
cotacao_dolar = float(cotacao_texto)  # Tipo: Ponto Flutuante (float)

# ==============================================================================
# PROCESSAMENTO E LÓGICA (Operações com Tipos de Dados)
# ==============================================================================
# 1. Divisão simples para descobrir o montante em moeda estrangeira
orcamento_dolar = orcamento_reais / cotacao_dolar

# 2. Descobrindo a média de gastos diária disponível
gasto_diario_disponivel = orcamento_dolar / quant_dias

# 3. Operador de Comparação criando um Tipo de Dado Booleano (True ou False)
orcamento_valido = gasto_diario_disponivel >= VALOR_MINIMO_DIARIO_USD

# ==============================================================================
# FUNÇÕES DE SAÍDA (Exibição e Formatação de Strings)
# ==============================================================================
print("\n" + "="*45)
print(f"        RESUMO DO PLANEJAMENTO: {destino.upper()}        ")
print("="*45)
print(f"Duração da estadia: {quant_dias} dias")
print(f"Orçamento Convertido: U$ {orcamento_dolar:.2f}")
print(f"Disponibilidade diária: U$ {gasto_diario_disponivel:.2f}/dia")
print(f"Mínimo recomendado: U$ {VALOR_MINIMO_DIARIO_USD:.2f}/dia")
print("-"*45)

# Exibindo o booleano de forma amigável dentro da f-string
print(f"Dentro do orçamento recomendado? {orcamento_valido}")
print("="*45)
print("Dica: Use o Modo Interativo do Python para validar novos cálculos!")