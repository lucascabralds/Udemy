"""

OPeradores Lógicos - Aula 4
and, or, not
in e not in

"""

#nome= "Luiz Otávio."

#if 'vio' not in nome:
#   print("Executei.")
#else:
#    print("Existe o texto.")

usuario=input('Nome de usuário: ')
senha=input('Senha do usuário: ')

usuario_bd="luiz"
senha_bd='123456'

if usuario_bd ==usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')