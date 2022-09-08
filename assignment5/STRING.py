from multiprocessing.dummy import JoinableQueue


mainstring=input("enter main sentence: ")
splitstring=input("enter your string for slice sentence: ")
joinstring=input("enter your string for join sentence: ")
a=mainstring.split(splitstring)
b=joinstring.join(a)
print('your senetence convert to:',b)





