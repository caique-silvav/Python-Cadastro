from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'banco_de_dados.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado! Criando um novo arquivo...')
    criarArquivo(arq)



cabeçalho('SISTEMA DE CADASTRO DE PESSOAS v1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema', 'Excluir arquivo de dados'])
    if resposta == 1:
        cabeçalho('Opção 1')
        lerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        cabeçalho('Nova Pessoa Cadastrada')
        nome = str(input('Primeiro Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
        sleep(1)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
    elif resposta == 4:
        cabeçalho('Excluindo arquivo de dados...')
        deleteArquivo(arq)
        sleep(1)
    else:
        print('\033[0;31mERRO: Por favor, digite uma opção válida!\033[m')
        sleep(1)
    
