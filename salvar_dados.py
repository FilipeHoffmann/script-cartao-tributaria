import csv

class salvar_dados:
    def __init__(self,dados:list, nome_arquivo:str):
        self.nome_arquivo = nome_arquivo
        self.dados_array = dados
        
    def salvar_sem_cabecalho(self):
        with open(self.nome_arquivo,'a+', encoding='utf-8', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for i in range(len(self.dados_array)):
                escritor_csv.writerow(self.dados_array[i])
                
    def salvar(self):
        with open(self.nome_arquivo,'a+', encoding='utf-8', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(["CNPJ","Valor Total"])
            for i in range(len(self.dados_array)):
                escritor_csv.writerow(self.dados_array[i])