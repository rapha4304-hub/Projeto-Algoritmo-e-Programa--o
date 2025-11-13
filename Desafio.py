# DESAFIO DE AUTOMAÇÃO DE INSPEÇÃO DE PEÇAS

# 1. Padrões de Qualidade
PESO_MIN, PESO_MAX = 95, 105
CORES_PERMITIDAS = ['azul', 'verde']
COMP_MIN, COMP_MAX = 10, 20
CAPACIDADE_CAIXA = 10

todas_as_pecas = []
caixas = [[]]

# 2. Função de verificação


def verificar_peca(peso, cor, comp):

    lista_erros = []
    if not (PESO_MIN <= peso <= PESO_MAX):
        lista_erros.append("Peso")
    if cor not in CORES_PERMITIDAS:
        lista_erros.append("Cor")
    if not (COMP_MIN <= comp <= COMP_MAX):
        lista_erros.append("Comp.")
    return lista_erros

# 3. Função para evitar repetição


def obter_float(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Número inválido.")


def buscar_peca(peca_id):

    return next((p for p in todas_as_pecas if p['id'] == peca_id), None)


# 3. Menu interativo

def cadastrar():
    peca_id = input("  ID da peça: ").strip()
    if buscar_peca(peca_id):
        print("ID já existe.")
        return

    peso = obter_float(f"  Peso (g) de {peca_id}: ")
    cor = input(f"  Cor de {peca_id}: ").strip().lower()
    comp = obter_float(f"  Comprimento (cm) de {peca_id}: ")

    motivos = verificar_peca(peso, cor, comp)

    status = "Aprovada" if not motivos else "Reprovada"

    peca = {'id': peca_id, 'peso': peso, 'cor': cor,
            'comp': comp, 'status': status, 'motivos': motivos}
    todas_as_pecas.append(peca)

    if status == "Aprovada":
        print(f"  -> Peça {peca_id} APROVADA.")
        caixa_atual = caixas[-1]
        caixa_atual.append(peca_id)
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            print(f"[AVISO] Caixa {len(caixas)} cheia!.")
            caixas.append([])
    else:
        print(f"  -> Peça {peca_id} REPROVADA. Motivos: {motivos}")


def listar():
    if not todas_as_pecas:
        print("Nenhuma peça cadastrada.")
        return
    for peca_id in todas_as_pecas:

        status_str = f" ID: {peca_id["id"]} (Aprovada)" if peca_id[
            "status"] == "Aprovada" else f" ID: {peca_id["id"]} (Reprovada, Motivos: {peca_id["motivos"]})"
        print(f"  {status_str}")


def remover():
    peca_id = input("  ID para remover: ").strip()
    peca_encontrada = buscar_peca(peca_id)

    if not peca_encontrada:
        print(f"ID {peca_id} não encontrado.")
        return

    todas_as_pecas.remove(peca_encontrada)

    if peca_encontrada["status"] == "Aprovada":
        for caixa in caixas:
            if peca_id in caixa:
                caixa.remove(peca_id)
                break
    print(f"-> Peça {peca_id} removida.")


def ver_caixas():

    for i, caixa in (caixas):
        numero_caixa = i + 1
        status = "(Fechada)" if numero_caixa < len(caixas) else "(Em uso)"
        print(
            f"Caixa {numero_caixa} {status} [{len(caixa)}/{CAPACIDADE_CAIXA}] Peças: {caixa}")


def relatorio():
    print("RELATÓRIO FINAl")
    aprovadas = sum(1 for p in todas_as_pecas if p['status'] == 'Aprovada')
    reprovadas = len(todas_as_pecas) - aprovadas

    erros = {'Peso': 0, 'Cor': 0, 'Comp.': 0}
    for p in todas_as_pecas:
        if p['status'] == 'Reprovada':
            for motivo in p['motivos']:
                erros[motivo] += 1

    print(f" Aprovadas: {aprovadas} | Reprovadas: {reprovadas}")
    print(
        f" Erros: Peso({erros['Peso']}), Cor({erros['Cor']}), Comp.({erros['Comp.']})")
    print(f" Caixas Fechadas: {len(caixas) - 1}")
    print(
        f" Peças na Caixa Atual (Caixa {len(caixas)}): {len(caixas[-1])} / {CAPACIDADE_CAIXA}")


# Menu interativo
menu_opcoes = {
    "1": ("Cadastrar nova peça", cadastrar),
    "2": ("Listar peças aprovadas/reprovadas", listar),
    "3": ("Remover peça cadastrada", remover),
    "4": ("Listar caixas fechadas", ver_caixas),
    "5": ("Gerar relatório final", relatorio)
}

print("Bem-vindo ao Sistema de Gestão de Peças!")

while True:
    print("Menu de opções:")

    for chave, (texto, _) in menu_opcoes.items():
        print(f" {chave}. {texto}")
    print(" 6. Sair")

    escolha = input("Escolha (1-6): ").strip()

    if escolha == "6":
        print("Encerrando...")
        break

    acao = menu_opcoes.get(escolha)

    if acao:
        print(f"\n--- {acao[0]} ---")
        acao[1]()
    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")
