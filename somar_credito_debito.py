class somar_credito_debito:
    def __init__(self,lista_cnpj_valor:list) -> None:
        self.lista_cnpj_valor = lista_cnpj_valor

    def somar(self):
        for i in range(len(self.lista_cnpj_valor)):
            self.lista_cnpj_valor[i][1] = float(self.lista_cnpj_valor[i][1]) + float(self.lista_cnpj_valor[i][2])
            self.lista_cnpj_valor[i].pop()
        return self.lista_cnpj_valor