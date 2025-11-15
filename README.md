# README.md -- DESAFIO DE AUTOMAÇÃO DE INSPEÇÃO DE PEÇAS

Este é um protótipo que simula um sistema de automação para inspeção de qualidade de peças industriais, permitindo cadastrar peças, validação com critérios predefinidos, organizando em caixas para posteriormente gerar relatórios da produção.


## Critérios de Qualidade (Conforme Orientação “Entrega de Trabalho”)

Peso: Deve estar entre 95g e 105g.

Cor: Deve ser 'azul' ou 'verde'.

Comprimento: Deve estar entre 10cm e 20cm.

## Funcionalidades do Menu

1.  Cadastrar nova peça:
•	Solicita ao usuário um ID único, peso, cor e comprimento.
•	A função (verificar_peca) é chamada para validar os atributos.
•	Se a peça for aprovada, ela é adicionada à caixa atual (caixas[-1]).
•	Se a caixa atual atingir a capacidade (10 peças), o sistema avisa que a caixa está cheia e cria uma nova caixa vazia para as próximas peças.
•	Se a peça for reprovada, o sistema informa os motivos e não a adiciona.

2.  Listar peças aprovadas/reprovadas:
•	Exibe todas as peças cadastradas no sistema, mostrando seu ID, status e os motivos da reprovação (se aplicável).

3.  Remover peça cadastrada:
•	Solicita o ID da peça a ser removida.
•	A peça é removida da lista todas_as_pecas.
•	Se a peça é "Aprovada", também é possível remover da caixa.

4.  Listar caixas fechadas:
•	Mostra todas as caixas, indicando se estão cheias ou em uso.
•	Exibe a contagem de peças e a lista de IDs de peças dentro de cada caixa.

5.  Gerar relatório final:
•	Calcula e exibe um resumo estatístico da operação:

6.  Sair:
•	Encerra a execução do programa.

### Como rodar o programa (Passo a passo para executar em Python)

**Para executar, você precisa ter o Python 3 instalado em sua máquina**.

1.	Salve o Código: Salve o conteúdo do script em um arquivo com a extensão .py, por exemplo: automacao_pecas.py.
2.	Abra o Terminal: Abra um terminal no (Prompt de Comando no Windows, Terminal no macOS ou Linux) ou IDEs como PyCharm e VS Code e IDLE; que já está incorporado ao python.
3.	Navegue até a Pasta: Use o comando cd para navegar até o diretório onde você salvou o arquivo.
cd /caminho/para/sua/pasta

4.	Execute: Digite python seguido do nome do arquivo:
python automacao_pecas.py

5.	O programa iniciará e exibirá o menu principal. Basta digitar a opção (1 a 6) e pressionar ENTER. 

### Exemplos de Entradas e Saídas

**Exemplo 1: Tela Inicial do Menu ao executar o programa**.

Bem-vindo ao Sistema de Gestão de Peças! 
Menu de opções: 
1. Cadastrar nova peça 
2. Listar peças aprovadas/reprovadas 
3. Remover peça cadastrada 
4. Listar caixas fechadas 
5. Gerar relatório final 
6. Sair Escolha (1-6):

**Exemplo 2: Cadastrando uma nova peça**.
Escolha (1-¨6): Opção escolhida (1)
ID da peça: 123
Peso (g) de 123: 95
Cor de 123: azul
Comprimento (cm) de 123: 10
Peça 123: APROVADA.

