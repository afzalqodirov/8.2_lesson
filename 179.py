a1, a2, a3 = map(int, input().split()) 
b1, b2, b3 = map(int, input().split())  

t1 = min(a1, b1)
a1 -= t1
b1 -= t1
t2 = min(a1, b3)
a1 -= t2
b3 -= t2
total = t1 + t2  
t3 = min(a2, b2)
a2 -= t3
b2 -= t3
t4 = min(a2, b3) 
a2 -= t4
b3 -= t4
total += t3 + t4

t5 = min(a3, b1 + b2 + b3)  
total += t5
print(total)
