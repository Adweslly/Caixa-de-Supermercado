def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um valor inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mCampo não foi preenchido pelo usuario.\033[m")
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista, msg):
    cabecalho(msg)
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaInt("Escolha a opção: ")
    return opc
