import random

def rand():
    return random.random()*4-2 #random() 0-1인 실수를 생성.

n=100000
c=0; r=0 # c는 원에 맞는 횟수, r은 정사각형에 맞는 횟수
for i in range(n):
    x=rand()
    y=rand()
    if(-1<=x and x<=1) and (-1<=y and y<=1):
        r=r+1
    if(x**2+y**2<1):
        c=c+1
PI=4*c/r
print(PI)