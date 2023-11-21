from repositorio import banco
from use_cases.adicionar import adicionarProduto

def listarProduto():
    print('____ LISTA DE PRODUTOS ____')
    for produto in banco:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")

