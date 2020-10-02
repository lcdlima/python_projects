LISTA_DDD = [61,71,11,21,32,19,27,31]
LISTA_CIDADES = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']

NUMERO = int(input())

if not NUMERO in LISTA_DDD:
    print ('DDD nao cadastrado')
else:
    N = LISTA_DDD.index(NUMERO)
    print (LISTA_CIDADES [N])