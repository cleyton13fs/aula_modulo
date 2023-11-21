from use_cases.adicionar import adicionarProduto
from use_cases.listar import listarProduto
from use_cases.editar import editarProduto
from use_cases.deletar import deletarProduto
def menu():
    while True:
        print('__ MENU DE PRODUTOS __')
        print('1 - cadastrar produto')
        print('2 - editar produto')
        print('3- Deletar produto')
        print('4- listar produto')
        print('5 - sair')
        opcao = input('Selecione a opçao: ')
        if opcao == '1':
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            adicionarProduto(nome, categoria, preco)
        elif opcao == '2':
            codigo = int(input('Digite o codigo do produto: '))
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            editarProduto(codigo, nome, categoria, preco)
        elif opcao == '3':
            codigo = int(input('Digite o codigo do produto: '))
            deletarProduto(codigo)
        elif opcao == '4':
            listarProduto()
        else:
            print('Você saiu do programa!: ')
menu()