from arquivos_pasta import arquivos_pasta
from unificar_arquivos import unificar_arquivos
from unificar_por_cnpj import unificar_por_cnpj
from somar_credito_debito import somar_credito_debito
from salvar_dados import salvar_dados

if __name__ == "__main__":
    arquivo = arquivos_pasta("arquivos_do_mes")
    nome_arquivo = arquivo.retornar_arquivos()[1].split('_')
    ano = nome_arquivo[2]
    mes = nome_arquivo[3]
    unificar = unificar_arquivos(arquivo)
    dados_unificados = unificar.unificar()
    salvar_log = salvar_dados(dados_unificados,f"log_{mes}_{ano}.csv")
    salvar_log.salvar_sem_cabecalho()
    unificado_cnpj = unificar_por_cnpj(dados_unificados)
    cnpj = unificado_cnpj.unificar()
    soma = somar_credito_debito(cnpj)
    total = soma.somar()
    salvar = salvar_dados(total,f"soma_total_{mes}_{ano}.csv")
    salvar.salvar()
    pass