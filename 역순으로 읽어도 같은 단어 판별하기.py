def equal(word):
    i=len(word)
    j=i//2
    for k in range(j):
        if word[k]!=word[i-1-k]:
            return False
        return True

def main():
    while True:
        word=input('단어 입력: ')
        if word=='quit':
            break;
        print(equal(word))

main()
