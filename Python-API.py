import requests
cep = input("Digite o CEP: ")
link = f'https://viacep.com.br/ws/{cep}/json'

try:
    requisicao = requests.get(link)

    if requisicao.status_code == 200:

        dic_requisicao = requisicao.json()

        print(f"CEP: {dic_requisicao['cep']}")
        print(f"Logradouro: {dic_requisicao['logradouro']}")
        print(f"Complemento: {dic_requisicao['complemento']}")
        print(f"Bairro: {dic_requisicao['bairro']}")
        print(f"Cidade: {dic_requisicao['localidade']}")
        print(f"UF: {dic_requisicao['uf']}")

    elif requisicao.status_code == 404:
        print('Não foi possível encontrar o endereço passado como parâmetro')
    elif requisicao.status_code == 500:
        print('Ocorreu algum erro no servidor')
    else:
        print(requisicao.status_code)

except ConnectionError:
    print('Erro de Conexão')
except Exception:
    print('Erro')

# Faz uma requisição HTTP para a URL informada desativando a verificação do certificado SSL.
requisicao = requests.get(url, verify=False)


#EXERCÍCIOS

# solicite ao usuário a sigla de uma UF e utilize a API abaixo para consultar e exibir os
# nomes de todos os municípios da UF informada.

"""
import requests

uf = input("Digite uma uf: ").upper()
link = f"http://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"

try:
    resposta = requests.get(link)

    if resposta.status_code == 200:

        dic_requisicao = resposta.json()

    if dic_requisicao:
        print(f"Municípios da UF {uf}:")

        for municipio in dic_requisicao:
            print(municipio['nome'])

    elif resposta.status_code == 404:
        print('Não foi possível encontrar o endereço passado como parâmetro')
    elif resposta.status_code == 500:
        print('Ocorreu algum erro no servidor')

    else:
        print("UF não encontrado ou sem municipios!")
except requests.exceptions.RequestException:
    print("Erro de conexão com a API.")"""

# Utilize a API abaixo para gerar uma listagem com os nomes de N usuários. Exiba a
# lista em ordem alfabética

import requests

try:
    n = int(input('Quantidade: '))
    resposta = requests.get(f'https://randomuser.me/api/?results={n}')

    if resposta.status_code == 200:
        dicionario = resposta.json()
        lista = dicionario['results']

        lista_nomes = []
        for item in lista:
            nome = item['name']
            lista_nomes.append(f"{nome['first']} {nome['last']}")
        lista_nomes.sort()
        for nome in lista_nomes:
            print(nome)
    else:
        print('Erro de requisição')
except Exception as erro:
    print(f'Erro: {erro}')