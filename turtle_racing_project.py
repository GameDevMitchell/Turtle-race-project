from turtle import Turtle, Screen
from random import randint

benny = Turtle("turtle")
tammy = Turtle("turtle")
tommy = Turtle("turtle")
tummy = Turtle("turtle")
freddy = Turtle("turtle")
penny = Turtle("turtle")
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
turtles = [benny, tammy, tommy, tummy, freddy, penny]
colour_pos = 0
y_pos = 0
turtle_pos = 0

for turtle in turtles:
    turtle.color(colours[colour_pos])
    turtle.penup()
    turtle.goto(x=-230, y=pos[y_pos])
    colour_pos += 1
    y_pos += 1

# start race
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 220:
            is_race_on = False

winners = [turtle for turtle in turtles if turtle.xcor() > 220]
winning_colours = [turtle.pencolor() for turtle in winners]

if len(winners) == 1:
    # Only one winner
    if winning_colours[0] == user_bet:
        print("Congrats✨🎉🎉✨")
    else:
        print("Oops! Bad luck😂")
    print(f"The {winning_colours[0]} turtle is the winner")
else:
    # Multiple winners
    if user_bet in winning_colours:
        print("Congrats✨🎉🎉✨")
    else:
        print("Oops! Bad luck😂")
    print(f"The {', '.join(winning_colours)} turtles are the winners")

screen.exitonclick()
