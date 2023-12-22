from CaixaDeLoja.interface import *
from CaixaDeLoja.funcao import *

carrinho = 'carrinho.txt'
estoque = 'estoque.txt'

if not existeArquivo(carrinho):
    criarArquivo(carrinho)

while True:
    resposta = menu(['Passar Produto', 'Ver Carrinho', 'Finalizar Compra', 'Finalizar Programa'], 'MENU PRINCIPAL')
    if resposta == 1:
        while True:
            resp = menu(['Digitar produto', 'Sair'], 'Registrando Compra')
            if resp == 1:
                item_cliente = input('Produto: ')
                quantidade_cliente = leiaInt('Quantidade: ')
                valor_produto = float(input('Valor: '))
                registrar(carrinho, item_cliente, quantidade_cliente, valor_produto)
            else:
                break
    elif resposta == 2:
        cabecalho('Carrinho')
        lerArquivo(carrinho)
    elif resposta == 3:
        cabecalho('Valor total da compra')
        somandoCompra(carrinho)
        finalizando('carrinho.txt')
        print(f"Obrigado pela preferencia. Volte sempre!")
    elif resposta == 4:
        cabecalho('Finalizando Programa...')
        break
    else:
        print("\033[31mERRO! Opção inválida, por favor digite uma opção valida.\033[m")
