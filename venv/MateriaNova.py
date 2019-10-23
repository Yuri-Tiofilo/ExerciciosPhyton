notas = dict()
notas2 = dict()
notas = {'Ana': 9.5, 'José': 8.2, 'Maria:': 9.8, 'João': 7.9}
#notas2 = {'Yuri': 9.5, 'Tiago': 8.2, 'Lucas': 9.8, 'Max': 7.9}

#get
# uma função do dicionario para procurar e devolver alguma coisa
#print(notas.get('Carla', 'Nome não encontrado'))

#utilizando in
#ele traz o valor de true ou false que existe dentro da chave, não procurando no valor
#para encontrar no valor é necessario colocar print(8.2 in notas.values()), encontrando o valor que esta dentro da chave
#print('José' in notas)

#inserindo novo elemento
#nome da chave = [uma variavel] = outra variavel
#notas['Carla'] = 8.7
#print(notas)

#deletando elemento
#del notas['Ana']
#print(notas)

#função para que se no caso ele não encontre o valor ele possa mandar uma mensagem
#print(notas.pop('Ana', 'Nome não encontrado'))
#print(notas.pop('Carlos', 'Nome não encontrado'))
#print(notas)

#Insere apenas valores diferentes que não existe no primeiro vetor
#Nome poderia ser  qualquer variavel
#for nome in notas2:
    #notas[nome] = notas2[nome]
#função pronta para inserir valores diferentes que não existe no primeiro vetor
#notas.update(notas2)
#print(notas)

#Inserindo uma atualização em todos os elementos do dicionario
#Está função vai percorrer o dicionario e vai adicionar +1 dentro de cada valor que esta dentro da chave
#é gerado um novo dicionario que coloca este novos valores
#nota_final = {nome: 1 + notas[nome] for nome in notas}
#print(nota_final)



