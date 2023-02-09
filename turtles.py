from turtle import Turtle, Screen 
import random 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = ""
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# loop until the user enters a valid colour
while len(user_bet) == 0:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Please enter a valid colour! ")

    if user_bet not in colours:
        user_bet = ""

# starting y positions of the turtles on the screen        
y_positions = [-70, -40, -10, 20, 50, 80,  110]
all_turtles = []

# loop through and create the turtles for the race
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    # lift the turtles pen "up" so nothing is drawn on the screen
    new_turtle.penup()
    # move the turtle to the left side of the screen to start the race
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True 

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:

            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
