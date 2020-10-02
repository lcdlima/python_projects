# In an imaginary country called Lisarb, all inhabitants are happy to pay their taxes, as they know that there are no corrupt politicians and the funds raised are used for the benefit of the population, without any deviation. The currency of this country is Rombus, whose symbol is R $.
# Read a value to two decimal places, equivalent to the salary of a person from Lisarb. Then calculate and show the amount that this person must pay Income Tax

SALARIO = float(input())

if SALARIO >= 0 and SALARIO <= 2000:
    print ('Isento')
elif SALARIO > 2000 and SALARIO <= 3000: 
    IMPOSTO = (SALARIO - 2000)*0.08
    print ('R$ {:.2f}'.format (IMPOSTO))
elif SALARIO > 3000 and SALARIO <=4500: 
    IMPOSTO = (SALARIO - 3000)*0.18 + 80
    print ('R$ {:.2f}'.format (IMPOSTO))
elif SALARIO > 4500:
    IMPOSTO = (SALARIO - 4500)*0.28 + 80 + 270
    print ('R$ {:.2f}'.format (IMPOSTO))