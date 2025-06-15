s = 0
a = int(input()) - 1

def multiplier(k):
    if '0' in k:
        return 0
    result = 1
    for i in k:
        result *= int(i)
    return result

start = int('1'+ '0'*a)

for i in range(start, start*10):
    s += multiplier(str(i))

print(s)
