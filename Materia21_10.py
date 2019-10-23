nome = input('Coloque o nome do arquivo:')
arquivo = open(nome,'r')

for linha in arquivo:
    print(linha)
    palavras = linha.spli()
    for palavra in palavras:
        print(palavra)