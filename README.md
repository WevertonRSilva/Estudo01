# Simulador de Orçamento de Viagem - Fundamentos Python

## Motivo do Projeto
Este projeto foi desenvolvido com o objetivo prático de centralizar e aplicar os conceitos mais fundamentais da linguagem Python. Através de um cenário real de planejamento financeiro para viagens internacionais, o script demonstra como o interpretador gerencia a entrada de dados do usuário, converte esses dados em tipos manipuláveis, processa regras de negócio e os exibe de forma tratada no terminal.

## Conceitos Core Praticados

### 1. Tipos de Dados
O script manipula ativamente quatro tipos de dados primitivos essenciais:
* **`str` (String):** Utilizado no nome do destino e no tratamento inicial dos inputs.
* **`int` (Inteiro):** Utilizado na contagem absoluta dos dias de viagem.
* **`float` (Flutuante):** Essencial para precisão monetária (orçamentos e cotações de moedas).
* **`bool` (Booleano):** Resultado lógico (`True` ou `False`) da validação do orçamento diário.

### 2. Variáveis vs. Constantes
* **Variáveis:** Dados que mudam a cada execução (ex: `destino`, `quant_dias`). Escritas em *snake_case* e minúsculas conforme a PEP 8.
* **Constantes:** Valores de referência estáticos que guiam as regras do sistema (ex: `VALOR_MINIMO_DIARIO_USD`). Por convenção da linguagem, são declaradas estritamente em letras maiúsculas para indicar que seu valor não deve ser mutável ao longo do script.

### 3. Funções de Entrada e Saída
* **`input()`:** Captura os dados digitados. É documentado e tratado que esta função **sempre** retorna um tipo `str`.
* **`print()`:** Exibe o layout do terminal. Utiliza recursos de **f-strings** (`f"..."`) combinados com especificadores de formato (`:.2f`) para forçar o arredondamento de duas casas decimais em tipos float.

### 4. Conversão de Tipos (Casting)
Como a entrada via terminal é puramente textual, o projeto demonstra o uso explícito de `int()` e `float()` para transformar dados e evitar erros de operações inválidas (como tentar dividir uma string por outra).

---

## Como Executar o Projeto

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone este repositório:
   ```bash
   https://github.com/WevertonRSilva/Estudo01.git
