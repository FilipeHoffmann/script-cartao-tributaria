# bot-cartao-tributaria

Bot para a formatação dos dados fornecidos pelo SEFAZ.

## Objetivo:

- Somar todos os valores (crédito e débito) por CNPJ sem distinção de banco.
- Converter os dados nos arquivos .txt presentes na pasta arquivos_do_mes para uma planilha.

## Passo a passo

1. Copie os arquivos .txt contendo os as informações e cole na pasta **arquivos_do_mes**.
2. Dê um duplo clique no arquivo ```main.exe``` para executar o programa.
3. Após alguns segundos será gerado os arquivos: ```log_{mes}_{ano}.csv``` e ```soma_total_{mes}_{ano}.csv```.

## Soma total

O arquivo soma_total demonstra os CNPJ e o valor total arrecadado.

## Log:

O arquivo log demonstra todos os dados que foram utilizados para a formação do arquivo soma total para uma possível conferência.
