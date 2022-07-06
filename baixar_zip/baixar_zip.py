import shutil
import zipfile
import requests
import os
from datetime import date


print('Iniciando')

urls = [
    (
        "ABC1234",
        "http://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?jornal=529&pagina=1&data=13/11/2017&captchafield=firstAccess"
    ),
    (
        "ABC4444",
        "http://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?jornal=529&pagina=1&data=13/11/2017&captchafield=firstAccess"
    )
    ]


def gerarPdf(nome_arquivo, url, pasta):
    print('Gerando arquivo' + nome_arquivo)
    resp = requests.get(url)
    with open(pasta + "/" + nome_arquivo, "wb") as code:
        code.write(resp.content)


def adicionarZip(nome_arquivo):
    print('Zipando arquivo')
    z = zipfile.ZipFile('final.zip', 'a', zipfile.ZIP_DEFLATED)
    z.writestr("./" + nome_arquivo)
    z.close()


def zipar(arqs):
    with zipfile.ZipFile('teste.zip','w', zipfile.ZIP_DEFLATED) as z:
        for arq in arqs:
            if(os.path.isfile(arq)): # se for ficheiro
                z.write(arq)
            else: # se for diretorio
                for root, dirs, files in os.walk(arq):
                    for f in files:
                        z.write(os.path.join(root, f))

data_atual = date.today()
nome_pasta = ("./%s" % (data_atual))

if os.path.isdir(nome_pasta):
    shutil.rmtree(nome_pasta)

os.makedirs(nome_pasta)

for data in urls:
    nome_arquivo = data[0] + ".pdf"
    gerarPdf(nome_arquivo, data[1], nome_pasta)


zipar([nome_pasta, 'Tudo'])
shutil.rmtree(nome_pasta)

