nome = "Luiz Otávio"
idade = 32 #int
altura = 1.80 #float
e_maior = idade > 18 #bool
peso = 80
imc = peso / (altura **2)


print(nome, 'tem', idade, ' anos de idade e seu imc é',imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{im:.2f} {n} tem {i} anos e seu imc é '.format(n=nome, i=idade,im=imc))
