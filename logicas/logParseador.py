import re
import os
#blacklist = {"dhcpd", "named[", "snmpd" }

iplist=[]

def leLogsLimpando(local):
    global iplist
    with open(local) as linha:
        for linhaFinal in linha:

            iplist.append(quebraLogs(linhaFinal))

    return removeNullIguais()

def quebraLogs(linha):

    try:
        return re.findall(r'DST=(.*?) LEN=', linha)
    except ValueError:
        return ""

def debug(caminho):
    """
    so pra testes
    :return:
    """
    if caminho == "":
        return leLogsLimpando(os.getcwd()+"\iptablesLog.txt")
    else:
        return leLogsLimpando(caminho)

def removeNullIguais():
    global iplist
    iplist = filter(None, iplist)
    last = []
    for item in iplist:
        if item not in last:
            last.append(item)

    return last


if __name__ == "__main__":
    debug()