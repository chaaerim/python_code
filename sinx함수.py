def fact(num):
    f=1
    for i in range(1, num+1): # 시작점 1로 적어줘야함 곱셈이므로..!
        f=f*i
    return f

def sin(x):
    s=0
    sign=1
    for n in range(1, 2*10, 2):
        s+=sign*x**n/fact(n)
        sign=-sign
    return s
print('sin(0.5)=', sin(0.5))
print('sin(3.14159/2)', sin(3.14159/2))