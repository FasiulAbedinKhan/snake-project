import turtle
import time
import random

delay=0.1
score = 0
highscore = 0


#set up the screen

screen = turtle.Screen()
screen.title("Snake Game V1.1")
screen.bgcolor("#545AA7")
screen.setup(width=680, height=680)
screen.tracer(0)

#setting the border
border = turtle.Turtle()
border.speed(0)
border.penup()

border.shape("square")
border.shapesize(25,25)
border.color("#f9ccca")



#snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#111622")
head.penup()
head.goto(0,0)
head.direction="stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#cc0000")
food.penup()
food.goto(0,100)

segments = []

#scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.goto(0,280)
scoreboard.write("Score: {}  High Score: {}".format(score,highscore),align="center",font=("Arial",24,"normal"))


#function
def go_up():
    if head.direction !="down":
        head.direction ="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_right():
    if head.direction !="left":
        head.direction="right"
def go_left():
    if head.direction !="right":
        head.direction="left"

#movement
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)             #can also be written like
                                    #head.setx(head.xcor()+20)

#keyboard
screen.listen()
screen.onkeypress(go_up,"w")
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_right,"d")
screen.onkeypress(go_right,"Right")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_left,"Left")

#mainloop

while True:
    screen.update()

    #check for collisions with wall
    if head.xcor()>250 or head.xcor()<-250 or head.ycor()>250 or head.ycor()<-250:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #why hide the segments
        for segment in segments:
            segment.goto(800,800)

        #clear the segments list
        segments.clear()

        #reset the score
        score =0

        #reset the delay
        delay=0.1

        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score,highscore),align="center",font=("Arial",24,"normal"))


    #check for collisions with food
    if head.distance(food)<20:
        #move the food to a random position
        x= random.randint(-250,250)
        y= random.randint(-250,250)
        food.goto(x,y)

        # add new segments

        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#222d44")
        new_segment.penup()
        segments.append(new_segment)
        
        delay = delay - 0.001

        #increase the score
        score += 1
        if score > highscore:
            highscore = score
        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score,highscore),align="center",font=("Arial",24,"normal"))

    #move the end seg in rev order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    # move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)



    move()

    # body check
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # why hide the segments
            for segment in segments:
                segment.goto(800,800)

        #clear the segments list
            segments.clear()

        #reset the score
            score=0
        #reset the delay
            delay =0.1
        #update the scoreboard
        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score,highscore),align="center",font=("Arial",24,"normal"))


    time.sleep(delay)

screen.mainloop()


