n = int(input())

temp = []
for i in range(n):
    a, b = map(int, input().split())
    temp.append((a,b,i))
# grok.com sal qarashib yubordi lambda joyini
temp.sort(key=lambda x: (x[0] / x[1], x[2]))
for i in temp:
    print(i[0], i[1])
