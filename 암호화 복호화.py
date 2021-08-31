def encrypt(text):
    enc_text=''
    for c in text:
        n=ord(c)
        enc_text=enc_text+chr(n+1)
    return enc_text

def decrypt(enc_text):
    dec_text=''
    for c in enc_text:
        n=ord(c)
        dec_text=dec_text+chr(n-1)
    return dec_text

def main():
    text=input('평문: ')
    enc_text=encrypt(text)
    print('암호문: ', enc_text)
    dec_text=decrypt(enc_text)
    print('복호화 결과: ', dec_text)

main()
