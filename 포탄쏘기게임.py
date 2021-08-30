from tkinter import *
import time
import random
WIDTH = 800; HEIGHT = 400
class Ball:
    def __init__(self, canvas, color, size, x, y, xspeed, yspeed):
        self.canvas = canvas # 캔버스 객체
        self.color = color # Ball의 색상
        self.size = size # Ball의 크기
        self.x = x; self.y = y # Ball의 x,y좌표
        self.xspeed = xspeed; self.yspeed = yspeed # Ball의 수직방향 속도
        self.id = canvas.create_oval(x, y, x+size, y+size, fill=color,outline=color)

    def move(self): # Ball을 이동시키는 함수
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1, y1, x2, y2) = self.canvas.coords(self.id) # 공의 현재 위치를 얻는다.
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= WIDTH: # 공의 x 좌표가 경계를 넘으면
            self.xspeed = - self.xspeed # 속도의 부호를 반전시킨다.
        if y1 <= 0 or y2 >= HEIGHT: # 공의 y 좌표가 경계를 넘으면
            self.yspeed = - self.yspeed # 속도의 부호를 반전시킨다.

bullets = [] # 생성된 포탄을 저장하는 리스트
def fire(event):
    bullets.append(Ball(canvas, "blue", 10, 150, 250, 10, 0))
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<Button-1>", fire)

spaceship = Ball(canvas, "green", 100, 100, 200, 0, 0)
enemy = Ball(canvas, "red", 100, 500, 200, 0, 5)
while True:
    for bullet in bullets:
        bullet.move()
# 포탄이 화면을 벗어나면 삭제한다.
        if (bullet.x+bullet.size) >= WIDTH:
            canvas.delete(bullet.id)
            bullets.remove(bullet)
    enemy.move()
    window.update()
    time.sleep(0.03)
