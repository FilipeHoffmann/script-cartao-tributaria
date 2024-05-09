from arquivos_pasta import arquivos_pasta
from unificar_arquivos import unificar_arquivos
from unificar_por_cnpj import unificar_por_cnpj

if __name__ == "__main__":
    arquivo = arquivos_pasta("arquivos_do_mes")
    unificar = unificar_arquivos(arquivo)
    dados_unificados = unificar.unificar()
    unificado_cnpj = unificar_por_cnpj(dados_unificados)
    cnpj = unificado_cnpj.unificar()
    for i in range(len(cnpj)):
        print(cnpj[i])
    pass