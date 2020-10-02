# Read four numbers (N1, N2, N3, N4), each with one decimal place, corresponding to a student's four grades. Calculate the average with weights 2, 3, 4 and 1, respectively, for each of these notes and show this average accompanied by the message "Media:". If this average is greater than or equal to 7.0, print the message "Student approved.". If the calculated average is less than 5.0, print the message "Student failed." If the calculated average is between 5.0 and 6.9, including these, the program should print the message "Student in exam.".
# In case the student is in exam, read a value corresponding to the exam score obtained by the student. Then print the message "Examination note:" accompanied by the note entered. Recalculate the average (add the exam score to the average previously calculated and divide by 2). and print the message "Student approved." (if the final grade is 5.0 or more) or "Student failing.", (if the grade is 4.9 or less). For these two cases (pass or fail after taking the exam), present in the last line a message "Final media:" followed by the final average for that student.

ENTRADA = input()

LISTA = ENTRADA.split()

N1 = float(LISTA[0])
N2 = float(LISTA[1])
N3 = float(LISTA[2])
N4 = float(LISTA[3])

MEDIA = (N1*2 + N2*3 + N3*4 +N4*1)/10
print ('Media: {:.1f}'. format (MEDIA))

if MEDIA >=7.0:
    print ('Aluno aprovado.')
elif MEDIA<5.0:
    print ('Aluno reprovado.')
else:
    print ('Aluno em exame.')
    NOTA_EXAME = float(input())
    print ('Nota do exame: {:.1f}'. format (NOTA_EXAME))
    MEDIA_FINAL = (MEDIA + NOTA_EXAME)/2
    if MEDIA_FINAL >= 5.0:
        print ('Aluno aprovado.')
    else:
        print ('Aluno reprovado.')
    print ('Media final: {:.1f}'. format (MEDIA_FINAL))