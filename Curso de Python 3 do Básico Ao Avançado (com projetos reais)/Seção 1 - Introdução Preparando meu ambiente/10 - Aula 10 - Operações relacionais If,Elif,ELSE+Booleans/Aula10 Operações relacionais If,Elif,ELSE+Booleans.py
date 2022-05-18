"""
Operadores Relacionais
= > >= <= !=

== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

# Limite para pegar empréstimo
idade_menor=20 #Muito jovem
idade_maior=30 #Maior de idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} Não pode pegar o emprestimo')