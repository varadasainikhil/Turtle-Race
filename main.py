import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["purple", "yellow", "red", "blue", "black", "orange"]
x = -230
y = 100
contestants = []
for i in range(6):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x, y)
    y -= 50
    contestants.append(turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ?")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in contestants:
        if i.xcor() < 230:
            random_distance = random.randint(0, 10)
            i.forward(random_distance)
        else:
            if i.color == user_bet:
                print("You have won the bet")
                is_race_on = False
                break
            else:
                print(f"You lose, {i.color()[0]} has won")
                is_race_on = False
                break

screen.exitonclick()
