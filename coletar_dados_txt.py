class coletar_dados_txt:
    def __init__(self,nome_arquivo:str) -> None:
        self.nome_arquivo:str = nome_arquivo
        self.dados_arquivo:list = []
        
    def instanciar_dados(self) -> list:
        with open(self.nome_arquivo, mode='r', encoding='utf-8', newline='') as arquivo_txt:
            arquivo_txt.readline()
            linhas = arquivo_txt.readlines()
            for linha in linhas:
                if linha == '\x00':
                    continue
                dados_linha = linha.strip()
                self.dados_arquivo.append(dados_linha)
        return self.dados_arquivo