from repositorio import banco
from use_cases.adicionar import adicionarProduto

def buscarPorCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if produto['codigo'] == codigo:
            return produto
    return None

