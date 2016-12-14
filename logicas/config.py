import re
arquivo="config.txt"
SENHA=""
CHAVE=""


apikey =""
apipass =""
teste="teste"


def leArquivosNM(local):
    """
    deve ler arquivos sem passar na memoria
    testar depois
    """
    with open(local) as arqui:
        for linha in arqui:
            print(linha)




def carregaCONF():
    global apikey
    global apipass
    try:
        confs = open(arquivo, 'r')
        info = confs.readlines()
        var = info[0]
        apipass = var[:36]
        apikey = var[-36:]
        dicionario = {'pass':apipass,'chav':apikey}

        confs.close()
        return dicionario
    except:
        print("configuracoes nao carregas, crie novo arquivo:\n")
        salvaCONF()

def carrego():
    print(apikey+apipass)


def salvaCONF():
    print("serao setados as chaves de apis utilizadas:")
    print("x-force ibm cloud")
    SENHA = input("senha:")
    CHAVE = input("chave")
    escreveARQ(SENHA,CHAVE)

def escreveARQ(senha,chave):
    arqui = open(arquivo,'w')
    arqui.write(senha+chave)
    arqui.close()


if __name__ == "__main__":
    leArquivosNM("/iptablesLog")