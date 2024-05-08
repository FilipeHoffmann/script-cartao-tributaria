import coletar_dados_txt
import arquivos_pasta
if __name__ == "__main__":
    dados_txt:list = coletar_dados_txt.coletar_dados_txt("exemplo/0016317068_47866934000174_2019_01_06022019_0201_0000235.txt")
    #print(dados_txt.instanciar_dados())
    arquivos = arquivos_pasta.arquivos_pasta("exemplo")
    for arquivo in arquivos.nomear_arquivos():
        print(arquivo)
    pass