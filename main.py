from arquivos_pasta import arquivos_pasta
from unificar_arquivos import unificar_arquivos
from unificar_por_cnpj import unificar_por_cnpj
from somar_credito_debito import somar_credito_debito
from salvar_dados import salvar_dados

if __name__ == "__main__":
    arquivo = arquivos_pasta("arquivos_do_mes")
    unificar = unificar_arquivos(arquivo)
    dados_unificados = unificar.unificar()
    unificado_cnpj = unificar_por_cnpj(dados_unificados)
    cnpj = unificado_cnpj.unificar()
    soma = somar_credito_debito(cnpj)
    total = soma.somar()
    print(total)
    salvar = salvar_dados(total)
    salvar.salvar()
    pass