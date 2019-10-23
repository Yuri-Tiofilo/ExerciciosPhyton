def tip3(cpf):
    retorno = 0
    stringcpf = str(cpf)
    if len(stringcpf) == 11:
        for i in range (0, 11):
            retorno = retorno + int(stringcpf[i])
        stringretorno = str(retorno)
        if stringretorno[0] == stringretorno[1] and len(stringretorno) == 2:
            return True
        else:
            return False
    else:
        return False

num = int(input("Digite seu cpf"))
print(tip3(num))