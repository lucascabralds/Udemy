'''

def duplicar(valor):
    return valor * 2
def triplicar(valor):
    return valor * 3
def quadriplicar(valor):
    return valor * 4




for valor in [2,4,6,8]:
    print(duplicar(valor))
    print(triplicar(valor))
    print(quadriplicar(valor))
    '''
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))