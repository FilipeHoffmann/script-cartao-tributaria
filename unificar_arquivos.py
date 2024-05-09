from coletar_dados_txt import coletar_dados_txt

class unificar_arquivos:
    def __init__(self,arquivos):
        self.arquivos = arquivos
        self.arquivos_gerais = []

    def unificar(self):
        for arquivo in self.arquivos.retornar_arquivos():
            coletar = coletar_dados_txt("arquivos_do_mes\\" + arquivo)
            for coleta in coletar.instanciar_dados():
                self.arquivos_gerais.append(coleta.split(";"))
        return self.arquivos_gerais