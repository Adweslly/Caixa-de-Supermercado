import os

from CaixaDeLoja.interface import *

estoque = 'estoque.txt'


def existeArquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("ERRO! Não foi possivel abrir a tela de registro de produtos.")
    else:
        print("Informe as informações solicitadas.")


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f"\033[31mNão foi possivel abrir o arquivo para leitura!\033[m")
    else:
        for item in a:
            dado = item.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f"{dado[0]:<25}{dado[1]:>3}")
    finally:
        a.close()


def registrar(arq, produto, quantidade, valor):
    try:
        a = open(arq, 'at')
    except:
        print(f"\033[31mNão foi possivel abrir o arquivo!\033[m")
    else:
        try:
            a.write(f"{produto};{quantidade};{valor}\n")
        except:
            print(f"\033[31mERRO! Não foi possivel ler o produto!")
        else:
            a.close()


def somandoCompra(arq):
    try:
        a = open(arq, 'rt')
    except:
        print(f"\033]31mERRO! Não foi possivel abrir o arquivo!")
    else:
        soma = 0
        for item in a:
            dado = item.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"Item: {dado[0]:<15}QTD: {dado[1]:} | Valor: {dado[2]}")
            qtd = float(dado[1])
            valor = float(dado[2])
            valor *= qtd
            soma += valor
        print(f"O valor total da compra foi de {soma}")
        while True:
            p = menu(['Cartão de Débito', 'Cartão de Crédito', 'Voucher', 'Pix', 'Dinheiro'], 'FORMA DE PAGAMENTO')
            if p == 1:
                print("Compra realizada com sucesso!")
            elif p == 2:
                print("Compra realizada com sucesso!")
            elif p == 3:
                print("Compra realizada com sucesso!")
            elif p == 4:
                print("Compra realizada com sucesso!")
            elif p == 5:
                din_cliente = float(input("Digite o valor: "))
                sobra = din_cliente - soma
                print(f'O troco do cliente foi de {sobra:.2f}')
                break
            else:
                print(f"\033[31mEscolha uma opção válida!\033[m")


def finalizando(arq):
    try:
        os.remove(arq)
    except:
        return f"\033[31mNão foi possivel excluir o arquivo!\033[m"
