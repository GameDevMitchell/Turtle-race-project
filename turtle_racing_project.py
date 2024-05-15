from turtle import Turtle, Screen
from random import randint

timmy = Turtle("turtle")
tammy = Turtle("turtle")
tommy = Turtle("turtle")
tummy = Turtle("turtle")
temmy = Turtle("turtle")
tibi = Turtle("turtle")
screen = Screen()
screen.title("Turtle race 🏎️🏁")
screen.setup(width=500, height=400)


user_bet = screen.textinput(
    title="Place your bet",
    prompt="Which turtle will win the race? Enter a colour"
    "(red/orange/yellow/green/blue/purple)",
)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = [-120, -70, -20, 30, 80, 130]
turtles = [timmy, tammy, tommy, tummy, temmy, tibi]
colour_pos = 0
y_pos = 0
turtle_pos = 0

for turtle in turtles:
    turtle.color(colours[colour_pos])
    turtle.penup()
    turtle.goto(x=-230, y=pos[y_pos])
    colour_pos += 1
    y_pos += 1

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winners = []
            winners.append(turtle)
            winning_colour = turtle.pencolor()
            if len(winners) > 1:
                winning_colour1 = winners[0]
                winning_colour2 = winners[1]
                if winning_colour1 or winning_colour2 == user_bet:
                    print("congrats✨🎉🎉✨")
                    print(
                        f"The {winning_colour1} and {winning_colour2} turtles are the winner"
                    )
                else:
                    print("Oops! Bad luck😂")
                    print(
                        f"The {winning_colour1} and {winning_colour2} turtles are the winner"
                    )
            if winning_colour == user_bet:
                print("congrats✨🎉🎉✨")
                print(f"The {winning_colour} turtle is the winner")
            else:
                print("Oops! Bad luck😂")
                print(f"The {winning_colour} turtle is the winner")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
