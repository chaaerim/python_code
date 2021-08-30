def printmenu():
    print('1. 섭씨 온도-> 화씨 온도')
    print('2. 화씨 온도-> 섭씨 온도')
    print('3. 종료')
    menunum=int(input('메뉴를 선택하세요: '))
    print()
    return menunum

def ctof():
    c=float(input('섭씨 온도를 입력하시오: '))
    f=c*9.0/5.0+32
    return f

def ftoc():
    f=float(input('화씨 온도를 입력하시오: '))
    c=(f-32.0)*5.0/9.0
    return c

def main():
    while True:
        menunum=printmenu()
        if menunum==1:
            f=ctof()
            print('화씨 온도=', f)
            print()
        elif menunum==2:
            c=ftoc()
            print('섭씨 온도=', c)
            print()
        else:
            break;
main()