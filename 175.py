
string = input()
k = len(string)
result = ''
i = 0
while i<k: 
    if string[i] == '(':
        temp = ''
        for j in range(i+1, len(string)):
            if string[j] == ')':i=j;break
            temp += string[j]
        result += temp[::-1]
    else:result += string[i]
    i+=1
print(result)
