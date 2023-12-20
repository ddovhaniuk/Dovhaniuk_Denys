import turtle
from turtle import Turtle, Screen
import random

print("ФАЙЛ ЗМІНЕНО ДЛЯ НОВОЇ ВІТКИ!")
screen = Screen()
screen.bgcolor("black")
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["vlad", "svyat", "dima", "max", "kolya", "oleg"]
count = 0
user_bet = screen.textinput(title="Make your bet:", prompt="which turtle will win?")

y = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for index in range(0, 6):
    new = Turtle(shape="turtle")
    new.color(colors[index])
    new.penup()
    new.goto(-230, y[index])
    all_turtles.append(new)

if user_bet:
    race_start = True

while race_start:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won! EAS", winning_color, "WIN")

            else:
                print("You LOSE! AHAHAH", winning_color, "WINNER, not", user_bet)

            race_start = False
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
