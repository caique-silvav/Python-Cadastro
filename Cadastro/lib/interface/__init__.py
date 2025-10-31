def LeiaInt (msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')  
            return 0
        else:
            return n
        

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for item in lista:
        print(f'\033[0;33m{lista.index(item) + 1}\033[m - \033[0;34m{item}\033[m')
    print(linha())
    opcão = LeiaInt('\033[0;32mSua Opção: \033[m')
    return opcão