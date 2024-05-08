import coletar_dados_txt
from arquivos_pasta import arquivos_pasta
from unificar_arquivos import unificar_arquivos
if __name__ == "__main__":
    """arquivos = arquivos_pasta.arquivos_pasta("arquivos_do_mes")
    for arquivo in arquivos.retornar_arquivos():
        dados_txt:list = coletar_dados_txt.coletar_dados_txt("arquivos_do_mes\\"+arquivo)
        for dado in dados_txt.instanciar_dados():
            print(dado)"""
    
    arquivo = arquivos_pasta("arquivos_do_mes")
    unificar = unificar_arquivos(arquivo)
    print(unificar.unificar())
    pass