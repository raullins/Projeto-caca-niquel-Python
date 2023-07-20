import random

MAX_LINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

LINHAS = 3
COLUNAS = 3

simbolos_contagem = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

simbolos_valores = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}




def checar_vitorias(colunas, linhas, aposta, valores):
    ganhos = 0
    linhas_vencedoras = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbolo_a_checar = coluna[linha]
            if simbolo != simbolo_a_checar:
                break
        else:
            ganhos += valores[simbolo] * aposta
            linhas_vencedoras.append(linha+1)

    return ganhos, linhas_vencedoras

def get_rodada_maquina(linhas, cols, simbolos):
    todos_simbolos = []
    for simbolo, simbolos_contagem in simbolos.items():
        # O underline serve para um valor qualquer dentro da lista
        for _ in range(simbolos_contagem):
            todos_simbolos.append(simbolo)

    colunas = []
    for _ in range(cols):
        coluna = []
        # Queremos uma copia da lista dos simbolos para poder atualizar com os valores que vamos tirar
        # e usamos "[:]" para fazer tal copia desta lista
        simbolos_atuais = todos_simbolos[:]
        for _ in range(linhas):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            coluna.append(valor)

        colunas.append(coluna)

    return colunas

def print_resultado_rodada_maquina(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) - 1:
                # "end" diz ao print que o final será um valor diferente do default que é "\n"
                print(coluna[linha], end= " | ")
            else:
                print(coluna[linha], end="")
        print()

def depositar():
    while True:
        quantidade = input("Quanto você quer depositar? R$")
        if quantidade.isdigit():
            quantidade = int(quantidade)
            if quantidade > 0:
                break
            else:
                print("Valor deve ser maior que 0.")
        else:
            print("Por favor, entre um número")

    return quantidade

def get_numero_de_linhas():
    while True:
        linhas = input("Digite a quantidade de linhas que você deseja apostar em (1-"+str(MAX_LINHAS)+")? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print("Entre uma quantidade válida de linhas.")
        else:
            print("Por favor, entre um número.")

    return linhas

def get_aposta():
    while True:
        quantidade = input("Quanto você quer apostar em cada linha? R$")
        if quantidade.isdigit():
            
            quantidade = int(quantidade)
            if MIN_APOSTA <= quantidade <= MAX_APOSTA:
                break
            else:
                print(f"Valor deve estar entre R${MIN_APOSTA} - R${MAX_APOSTA}.")
        else:
            print("Por favor, entre um número.")

    return quantidade

def jogo(carteira):
    linhas = get_numero_de_linhas()
    while True:
        aposta = get_aposta()
        valor_aposta_total = aposta * linhas

        if  carteira < valor_aposta_total:
            print (f"Você não possui saldo suficiente para apostar este valor. Saldo atual: R$ {carteira}")
        else:
            break
    
    print(f"Você está apostando R${aposta} em {linhas} linha(s). O valor total da aposta é R${valor_aposta_total}")
    print(f"Seu saldo restante é R$ {carteira-valor_aposta_total}")

    valores = get_rodada_maquina(LINHAS, COLUNAS, simbolos_contagem)
    print_resultado_rodada_maquina(valores)
    rodada, linhas_vencedoras = checar_vitorias(valores, linhas, aposta, simbolos_valores)
    print(f"Você ganhou R${rodada}.")
    print("Você ganhou nas linhas:", *linhas_vencedoras)

    return rodada - valor_aposta_total


def main():
    carteira = depositar()
    while True:
        print(f"Saldo atual: R${carteira}")
        resposta = input("Aperte 'Enter' para jogar ('s' para sair).")
        if resposta == "s":
            break
        carteira += jogo(carteira)

    print(f"Você saiu com R${carteira}")

main()