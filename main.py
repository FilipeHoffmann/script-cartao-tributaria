from arquivos_pasta import arquivos_pasta
from unificar_arquivos import unificar_arquivos
if __name__ == "__main__":
    arquivo = arquivos_pasta("arquivos_do_mes")
    unificar = unificar_arquivos(arquivo)
    for i in range(len(unificar.unificar())):
        print(unificar.unificar()[i])
    pass