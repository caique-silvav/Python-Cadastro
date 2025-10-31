from lib.interface import cabeçalho

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[0;32mArquivo {nome} criado com sucesso!\033[m')
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[0;31mErro ao ler o arquivo!\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split()
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
        
def cadastrarPessoa(nome, pessoa='desconhecido', idade=0):
    try:
        a = open(nome, 'at')
    except:
        print('\033[0;31mHouve um erro ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{pessoa} {idade}\n')
        except:
            print('\033[0;31mHouve um erro ao escrever os dados!\033[m')
        else:
            print(f'\033[0;32mNovo registro de {pessoa} adicionado.\033[m')
            a.close()
        
def deleteArquivo(nome):
    import os
    try:
        os.remove(nome)
    except FileNotFoundError:
        print('\033[0;31mArquivo não encontrado para exclusão!\033[m')
    except PermissionError:
        print('\033[0;31mPermissão negada para excluir o arquivo!\033[m')
    else:
        print(f'\033[0;32mArquivo {nome} excluído com sucesso!\033[m')