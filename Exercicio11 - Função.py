def exercicioOnze(numero, salario):

    if numero > 40:
        horasextra = numero - 40
        valor = horasextra * (salario * 2);
        salariofinal = valor + (numero * salario)
    else:
        salariofinal = salario * numero
    return salariofinal

horas = int(input('Digite a quantidade de horas semanais: '))
horassalario = int(input('Digite a quantidade de horas semanais: '))
final = exercicioOnze(horas, horassalario)
print(final)