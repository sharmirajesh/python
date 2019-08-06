tuplex=('w',3,'i','s','o','u','r','c','e')
print(tuplex)
tuplex=tuplex[:2]+tuplex[3:]
print(tuplex)
listx=list(tuplex)
listx.remove('c')
tuplex=tuplex(listx)
print(tuplex)
