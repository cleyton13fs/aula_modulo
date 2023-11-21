from use_cases.gerar_produto import criarProduto
from repositorio import banco, cod_atual
# codigo - nome - categoria - preço
def adicionarProduto(nome, categoria, preco):
    produto = criarProduto(nome, categoria, preco)
    banco.append(produto)
    print('Produto adicionado com sucesso!')


