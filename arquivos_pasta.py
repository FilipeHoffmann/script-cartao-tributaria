import os

class arquivos_pasta:
    def __init__(self, caminho: str):
        self.caminho:str = caminho
        self.arquivos = []

    def nomear_arquivos(self)-> list:
        arquivos = os.listdir(self.caminho)

        for arquivo in arquivos:
            self.arquivos.append(arquivo)

        return arquivos