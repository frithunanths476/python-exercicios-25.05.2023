salarioAtual = float(input('Insira o seu salário: '))
percentual = float(input('Insira o percentual de aumento: '))
porcentagem = (percentual/100)
aumento = porcentagem*salarioAtual
novo_salario = salarioAtual+aumento
print(f'O seu novo sálario é: {novo_salario}')