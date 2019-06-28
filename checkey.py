import requests
import json
#essa parte deve ser implementada no programa principal para que essas informações sejam visiveis
#eu coloquei um pedido da chave e da pesquisa para que eu pudesse testar
#os prints também sao apenas pra ver que ta saindo tudo certo

chave = input('chave: ')
searchh = input('o que voce quer saber? ')
try:
    requisicao = requests.get('https://factchecktools.googleapis.com/v1alpha1/claims:search?query='+searchh+'&key='+chave)
    inform = json.loads(requisicao.text)
    informacoes = inform['claims']
    #informacoes é uma lista
    for elem in informacoes:
        #elem sao dicionarios)
        for elemenkey in elem.items():
            if elemenkey[0] == 'text':
                texto = elemenkey[1]
                print('texto: ', texto)
            elif elemenkey[0] == 'claimant':
                requeredor = elemenkey[1]
                print('requeredor: ', requeredor)
            elif elemenkey[0] == 'claimDate':
                DataReclamacao = elemenkey[1]
                print('data da reclamação ', DataReclamacao)
            elif elemenkey[0] == 'claimReview':
                #print(type(elemenkey[1]))
                for elemkeysdicts in elemenkey[1]:
                    #print(type(elemkeysdicts))
                    for dici in elemkeysdicts.items():
                        if dici[0] == 'url':
                            fonte = dici[1]
                            print('fonte: ', fonte)
                        elif dici[0] == 'title':
                            titulo = dici[1]
                            print('titulo:', titulo)
                        elif dici[0] == 'reviewDate':
                            DataRevisao = dici[1]
                            print('Data de Revisão: ', DataRevisao)
                        elif dici[0] == 'textualRating':
                            veracidade = dici[1]
                            print('avaiação textual: ', veracidade)
        print('\n')
except Exception as erro:
    print('algo deu errado')
