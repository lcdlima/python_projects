SALARIO = float(input())

if SALARIO > 0 and SALARIO <= 400:
    print ('Novo salario: {:.2f}'.format (SALARIO + SALARIO*0.15))
    print ('Reajuste ganho: {:.2f}'.format (SALARIO*0.15))
    print ('Em percentual: 15 %')
elif SALARIO > 400 and SALARIO <= 800:
    print ('Novo salario: {:.2f}'.format (SALARIO + SALARIO*0.12))
    print ('Reajuste ganho: {:.2f}'.format (SALARIO*0.12))
    print ('Em percentual: 12 %')
elif SALARIO > 800 and SALARIO <= 1200:
    print ('Novo salario: {:.2f}'.format (SALARIO + SALARIO*0.1))
    print ('Reajuste ganho: {:.2f}'.format (SALARIO*0.1))
    print ('Em percentual: 10 %')
elif SALARIO > 1200 and SALARIO <= 2000: 
    print ('Novo salario: {:.2f}'.format (SALARIO + SALARIO*0.07))
    print ('Reajuste ganho: {:.2f}'.format (SALARIO*0.07))
    print ('Em percentual: 7 %')
elif SALARIO > 2000:
    print ('Novo salario: {:.2f}'.format (SALARIO + SALARIO*0.04))
    print ('Reajuste ganho: {:.2f}'.format (SALARIO*0.04))
    print ('Em percentual: 4 %')