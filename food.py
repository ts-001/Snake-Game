from turtle import  Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Blue")
        self.penup()
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

    def s(self):
        self.score += 1
        print(self.score)