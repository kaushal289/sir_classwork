'''
1234
123
12
1
'''
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
        n=n-1
    print("")
