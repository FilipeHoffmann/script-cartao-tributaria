from arquivos_pasta import arquivos_pasta
from unificar_arquivos import unificar_arquivos
if __name__ == "__main__":
    arquivo = arquivos_pasta("arquivos_do_mes")
    unificar = unificar_arquivos(arquivo)
    dados_unificados = unificar.unificar()
    for i in range(len(dados_unificados)):
        print(dados_unificados[i])
    pass