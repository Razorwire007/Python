a, b = 0,1
n = int(input('Number where series should end: '))
while a <= n:
    print(a)
    a, b = b, a+b
    
