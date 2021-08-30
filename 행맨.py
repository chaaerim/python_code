import random
infile=open('words.txt', 'r')
line=infile.readlines()
word=random.choice(line)
word=word.rstrip()
guesses=''
turn=10
while turn>0:
    fail=0
    for c in word:
        if c in guesses:
            print(c, end='')
        else:
            print('_', end='')
            fail+=1
    if fail==0:
        print('성공!')
        break
    print('')
    guess=input('추측: ')
    guesses+=guess
    if guess!=word:
        turn-=1
        print('틀림')
        print(turn, '기회남음')
    if turn ==0:
        print('패배 답은 ', word)
infile.close()
햣