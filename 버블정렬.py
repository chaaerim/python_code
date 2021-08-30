list=[]
for i in range(10):
    n=int(input('정수를 입력하세요: '))
    list.append(n)
print('정렬 전: ', list)
for i in range(0, len(list)):
    for j in range(0, len(list)-i-1):
        if list[j]<list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print('정렬 후: ', list)
