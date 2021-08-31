def reverse(word):
    l=len(word)
    newword=''
    for i in range(l-1, -1, -1):
        newword=newword+word[i]
    return newword

def main():
    while True:
        word=input('단어 입력: ')
        if word=='quit':
            break;
        print(reverse(word))

main()
