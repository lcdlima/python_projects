ENTRADA = input ()

LISTA = ENTRADA . split()

CODIGO = int (LISTA [0])
QUANTIDADE = int (LISTA[1])

if CODIGO == 1:
    PRECO = QUANTIDADE*4
    print ('Total: R$ {:.2f}'.format (PRECO))
elif CODIGO == 2:
    PRECO = QUANTIDADE*4.5
    print ('Total: R$ {:.2f}'.format (PRECO))
elif CODIGO == 3:
    PRECO = QUANTIDADE*5
    print ('Total: R$ {:.2f}'.format (PRECO))
elif CODIGO == 4:
    PRECO = QUANTIDADE*2
    print ('Total: R$ {:.2f}'.format (PRECO))
else:
    PRECO = QUANTIDADE*1.5
    print ('Total: R$ {:.2f}'.format (PRECO))