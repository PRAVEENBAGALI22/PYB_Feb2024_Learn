rows = 5
for i in range(0, rows):
    print('*', end='\n')
print('--------------------')
for i in range(0,rows-1):
    print('**',end='\n' )
print('--------------------')
for i in range(1,rows):
    for j in range(1,rows):
        print('*', end='')
    print()