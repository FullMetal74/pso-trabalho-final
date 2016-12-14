from requests.auth import HTTPBasicAuth
import requests
import json
import config
import socket
#vai ficar assim por hora
import logParseador
iplist=[]

def checaList():
    global iplist
    caminho = raw_input("caminho do arquivo:\n")
    iplist = logParseador.debug(caminho)
    for ip in iplist:
        print("teste >>".join(ip))
        resultado = pega(ip, config.apikey, config.apipass)
        print(resultado[u'history'][0][u'score'])
        if resultado[u'history'][0][u'score'] < 1:
            print("o ip: " + ip + " apresenta ameasas")


def checaManual():
    dic = config.carregaCONF()
    apikeys = dic['pass']
    apipasss = dic['chav']

    print("ensira o ip alvo:")
    ipadd= raw_input()
    try:
        socket.inet_aton(ipadd)
        pega(ipadd, config.apikey, config.apipass)

    except socket.error:
        print("invalido!")


def pegaWhois(ipalvo,apipass,apikey):
    a = requests.get('https://api.xforce.ibmcloud.com/whois/' + ipalvo, auth=HTTPBasicAuth(apikey, apipass) , verify=False)

    dicionario = json.loads(a.text)
    #print(dicionario)
    print("\n")
    return dicionario



def pega(ipalvo,apipass,apikey):
    print(apipass + " " + apikey)
    print("".join(ipalvo))
    a = requests.get('https://api.xforce.ibmcloud.com/ipr/history/' + "".join(ipalvo), auth=HTTPBasicAuth(apikey, apipass))
    dicionario = json.loads(a.text)
    print(dicionario)
    return dicionario




if __name__ == "__main__":

    #pega(raw_input("ayy"),config.apikey, config.apipass)

    pass