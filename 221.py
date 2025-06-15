a = int(input())
b = sorted(map(int, input().split()))

absolute = sorted(map(abs, b))
for i, x in enumerate(b):
    if x<0:
        temp = absolute.index(abs(x))
        absolute[temp] = -absolute[temp]
    else:break
print(*absolute)
