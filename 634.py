
string = input().split()

string.sort(key=lambda x:(x.count('a')), reverse=True)

print(*string)
