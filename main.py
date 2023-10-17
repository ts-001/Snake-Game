from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboaed
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake Game")
screen.tracer(0)
screen.bgcolor("black")


snake = Snake()
food = Food()
scoreb = Scoreboaed()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreb.increase_score()

   #collision with Walll
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreb.reset()
        snake.reset()

    #collision with tail
    for seg in snake.segment[1:len(snake.segment)]:
        if snake.head.distance(seg) < 10:
            scoreb.reset()
            snake.reset()
screen.exitonclick()