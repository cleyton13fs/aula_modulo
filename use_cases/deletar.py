from use_cases.buscar_por_codigo import buscarPorCodigo
from repositorio import banco


def deletarProduto(codigo: int) -> None:
    produto = buscarPorCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('Produto deletado comn sucesso!')
    else:
        print('Produto não encontrado!')

