from tabulate import tabulate as t
print('if you enter 2:''\n''we print (246)^-^''\n')
n=input("enter number:")
table=[n+str(int(n)*2)+str(int(n)*3)]
print(t(table,tablefmt='fancy'))