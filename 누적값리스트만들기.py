list=[10, 20, 30, 40, 50]
new=[sum(list[0:x+1]) for x in range(len(list))]
print('원래 리스트: ', list)
print('새로운 리스트: ', new)
