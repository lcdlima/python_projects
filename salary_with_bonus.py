# Make a program that reads the name of a salesman, his fixed salary and the total sales made by him in the month (in cash). Knowing that this seller earns 15% commission on his sales made, inform the total receivable at the end of the month, with two decimal places.

NOME = str (input ())

SALARIO_FIXO = float (input ())

TOTAL_VENDAS = float (input ())

TOTAL = SALARIO_FIXO + TOTAL_VENDAS*0.15

print ('TOTAL = R$ {:.2f}'. format (TOTAL))