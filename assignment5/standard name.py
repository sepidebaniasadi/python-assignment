from tabulate import tabulate as t


list_standardname=[]
list_name=[]
for i in range(10):
    name=input("name: ")
    list_name.append(name)
    first_letter=name[:1]
    caps= first_letter.upper()
    letters=name[1:]
    small=letters.lower()
    FINALLY=caps+small
    list_standardname.append(FINALLY)
table=[['name','standard name'],
[list_name[0],list_standardname[0]],
[list_name[1],list_standardname[1]],
[list_name[2],list_standardname[2]],
[list_name[3],list_standardname[3]],
[list_name[4],list_standardname[4]],
[list_name[5],list_standardname[5]],
[list_name[6],list_standardname[6]],
[list_name[7],list_standardname[7]],
[list_name[8],list_standardname[8]],
[list_name[9],list_standardname[9]]]
print(t(table,tablefmt='fancy_grid'))


    