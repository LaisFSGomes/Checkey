import requests     #para fazer requisições web
import json        #para trabalhar com saídas no formato de json

#--------------------------------------------------------------
def fazerRequisicao (pesquisa, chave):
    try:
        requicao = requests.get(('https://factchecktools.googleapis.com/v1alpha1/claims:search?query='+pesquisa+'&key='+chave+'&maxAgeDays=4')
        informacoes = json.loads(requicao.text)
        return informacoes
    except:
        print('Erro de conecção. Tente novamente')
        return None
#--------------------------------------------------------------
def printar (informacoes):
    #fazer ja ja

#--------------------------------------------------------------

pesq = input('escreva a notícia que você deseja verificar: ')

inf = fazerRequisicao(pesq)
