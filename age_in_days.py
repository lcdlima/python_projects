# Read an integer corresponding to a person's age in days and enter it in years, months and days
# Note: just to facilitate the calculation, consider every year with 365 days and every month with 30 days. In test cases there will never be a situation that allows 12 months and some days, such as 360, 363 or 364. This is just an exercise with the aim of testing simple mathematical reasoning.

IDADE = int(input())

ANOS = IDADE//365
print ('{} ano(s)'.format (ANOS))
IDADE = IDADE%365

MESES = IDADE//30
print ('{} mes(es)'. format (MESES))
IDADE = IDADE%30

DIAS = IDADE
print ('{} dia(s)'. format (DIAS))