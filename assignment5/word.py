from tabulate import tabulate as t

word=input("please enter you'r word: ")
for i in range(len(word)):
    # if word[i]=='a' or word[i]=='o' or word[i]=='u' or word[i]=='i' or word[i]=='e':
       A= word.split('a')
       A_REM="?".join(A)
       ASTR="".join(A_REM)
       I= ASTR.split('i')
       I_REM="?".join(I)
       ISTR="".join(I_REM)
       E= ISTR.split('e')
       E_REM="?".join(E)
       ESTR="".join(E_REM)
       U= ESTR.split('u')
       U_REM="?".join(U)
       USTR="".join(U_REM)
       O= USTR.split('o')
       O_REM="?".join(O)
       O_STR="".join(O_REM)     
       continue
table=[['word',word],
['word with out vowels',O_STR]]
print(t(table,tablefmt="fancy_grid"))




                
        


    

