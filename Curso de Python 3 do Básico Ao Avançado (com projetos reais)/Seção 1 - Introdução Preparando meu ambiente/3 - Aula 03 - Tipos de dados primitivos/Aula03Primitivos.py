"""
Tipos de dados - Os que já conhecemos
str - String - Textos
int - Inteiro
float - real/ponto flutuante
bool - verdadeiro-falso
"""

#quando usamos o type ela apresentara qual é tipo de dado
#sintaxe : type(varaivel ou texto em aspas)
print('Luiz', type('Luiz')) # apresenta qual e string, nesse caso seria str
print( 20,type(20)) # apresenta qual e string, nesse caso seria int
#Vale ressalta caso queiramos tratar dados int não se deve colocar o dado entre '' aspas.
print(25.23, type(25.23))#String float
print (10==10, type(10==10)) #String bool

#Timecashen

print('Luiz', type('Luiz'), bool('Luiz')) #Usando a tag bool você consegue validar uma ação ou um dado.

# Na linha abaixo o dado ele vai ser entrado como um tipo de dado str, após a a segunda virgula ele transformara aquele dado em int
print('10',type('10'), type(int('10')))
"""
Vale ressaltar que a sintaxe assim não é correto transformar valores que não convem a elas
como por exemplo um float para int
"""

#Exercicio da aula e fazer uma validação de cadastro.
#String: Nome
print('Lucas',type('Lucas'))

#Idade: int
print(20,type(20))

#Altura: float
print(1.70,type(1.70))

#É maior de idade 10>20
print(20>18,type(20>18))
