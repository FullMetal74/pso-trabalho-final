"""
https://zeltser.com/malicious-ip-blocklists/

"""

import sys

sys.path.append('logicas')

from logicas import apiLeitor
from logicas import config


def menu():
    print("=" * 60)
    print(" " * 25 + "opcoes")
    print("1 - leitura de logs iptables")
    print("2 - checar ip manualmente")
    print("0 - setar configuracao")

    opcao = raw_input("opcao\n")
    print("=" * 60)

    if(opcao == "1"):
        apiLeitor.checaList()
    if (opcao == "2"):
        apiLeitor.checaManual()
    elif(opcao == "0"):
        config.salvaCONF()


if __name__ == "__main__":
    #importante
    config.carregaCONF()
    menu()
