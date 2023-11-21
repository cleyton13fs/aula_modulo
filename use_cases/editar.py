from use_cases.buscar_por_codigo import buscarPorCodigo

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
       produto['nome'] = nome
       produto['categoria'] = categoria
       produto['preco'] = preco
       print('banco de dados alterados com sucesso!')
    else:
        print('Produto não encontrado')

