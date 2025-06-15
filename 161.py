n = int(input())
string = input().split()

# 'ASSALOM'
a = 2
s = 2
l = 1
o = 1
m = 1

A = 0
S = 0
L = 0
O = 0
M = 0
for i in string:
    if i == 'A':A+=1
    elif i == 'S':S+=1
    elif i == 'L':L+=1
    elif i == 'O':O+=1
    elif i == 'M':M+=1
if a<=A and s<=S and l<=L and o<=O and m<=M:print('YES')
else:print('NO')
