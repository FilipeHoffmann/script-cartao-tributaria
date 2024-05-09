class unificar_por_cnpj:
    def __init__(self, dados_unificados:list) -> None:
        self.dados_unificados:list = dados_unificados
        self.grouped_data = {}
        self.unificado_cnpj = []

    def unificar(self):
        # Percorre os dados para agrupar e somar
        for row in self.dados_unificados:
            key = row[0]  # A chave do dicionário é o primeiro elemento da linha
            values = [float(row[-2]), float(row[-1])]  # Os valores são os dois últimos elementos da linha
            if key not in self.grouped_data:
                self.grouped_data[key] = values
            else:
                self.grouped_data[key][0] += values[0]  # Soma o penúltimo elemento
                self.grouped_data[key][1] += values[1]  # Soma o último elemento

        for key, values in self.grouped_data.items():
            self.unificado_cnpj.append(f"{key};{values[0]};{values[1]}".split(";"))
        return self.unificado_cnpj