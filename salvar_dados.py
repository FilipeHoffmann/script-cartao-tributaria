import csv

class salvar_dados:
    def __init__(self,dados:list):
        self.nome_arquivo = "Soma_total.csv"
        self.dados_array = dados
                
    def salvar(self):
        with open(self.nome_arquivo,'a+', encoding='utf-8', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(["CNPJ","Valor Total"])
            for i in range(len(self.dados_array)):
                escritor_csv.writerow(self.dados_array[i])