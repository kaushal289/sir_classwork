'''
ABCD
EFG
HI
J
'''
ascii_number = 65
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        char=chr(ascii_number)
        print(char,end='')
        ascii_number += 1
    print("")
