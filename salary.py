# Write a program that reads an employee's number, his number of hours worked, the amount he receives per hour and calculates that employee's salary. Next, show the employee's number and salary, to two decimal places.

NUMBER = int (input ())

HOURS = int (input ())

VALUE_PER_HOUR = float (input ())

SALARY = HOURS*VALUE_PER_HOUR

print ('NUMBER = {}'. format (NUMBER))

print ('SALARY = U$ {:.2f}'. format (SALARY))