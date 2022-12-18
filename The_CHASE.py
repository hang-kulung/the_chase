import turtle
import random
import os

#windows
wn=turtle.Screen()
wn.setup(width=600, height=600)
wn.title("The Chase: 2Players")
wn.bgpic("bg.gif")
wn.tracer(0)

#games variables
game = False
help = False
s=0                    #timer
speed_ch=0.5
speed_run=0.7
q=30                    #cotrol size of chaser
w=20                    #control size of bullet
ammo=5

#adding the pictures
wn.addshape(os.path.expanduser("ufo_left.gif"))
wn.addshape(os.path.expanduser("ufo_rightt.gif"))
wn.addshape(os.path.expanduser("beam_up.gif"))
wn.addshape(os.path.expanduser("beam_down.gif"))
wn.addshape(os.path.expanduser("Octopus.gif"))
wn.addshape(os.path.expanduser("bullet.gif"))

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("Press Enter to Start", align="center", font=("Courier", 36, "normal"))

pen_a=turtle.Turtle()
pen_a.speed(0)
pen_a.color("white")
pen_a.penup()
pen_a.hideturtle()
pen_a.goto(0, -250)
pen_a.write("Press 'H' for Help", align="center", font=("Courier", 18, "normal"))




#chaser
ch=turtle.Turtle()
ch.speed(0)
ch.shape("Octopus.gif")
ch.penup()
ch.shapesize(stretch_wid=2, stretch_len=2)
ch.goto(-280, 0)
ch_x=0.5
ch_y=0

#runner
run=turtle.Turtle()
run.speed(0)
run.shape("ufo_left.gif")
run.penup()
run.goto(280, 0)
run_x= -0.7
run_y=0


#blocks
block=turtle.Turtle()
block.shape("beam_down.gif")
block.speed(0)
block.penup()
block.goto(-150, 290)
p=0.4

blocka=turtle.Turtle()
blocka.shape("beam_up.gif")
blocka.speed(0)
blocka.penup()
blocka.goto(0, -290)
e=0.4

blockb=turtle.Turtle()
blockb.shape("beam_down.gif")
blockb.speed(0)
blockb.penup()
blockb.goto(150, 290)
r=0.4

gun=turtle.Turtle()
gun.shape("bullet.gif")
gun.speed(0)
gun.penup()
gun.goto(400, 0)
shoot = False
gun_x=0
gun_y=0


# control chaser
def ch_up():
    global ch_x
    global ch_y
    ch_x=0
    ch_y= speed_ch


def ch_down():
    global ch_x
    global ch_y
    ch_x=0
    ch_y= speed_ch * -1


def ch_right():
    global ch_x
    global ch_y
    ch_x=speed_ch
    ch_y= 0

def ch_left():
    global ch_x
    global ch_y
    ch_x=speed_ch *-1
    ch_y= 0


#control runner

def run_up():
    global run_x
    global run_y
    run_x=0
    run_y= speed_run


def run_down():
    global run_x
    global run_y
    run_x=0
    run_y= speed_run * -1


def run_right():
    global run_x
    global run_y
    run_x=speed_run
    run_y= 0
    run.shape("ufo_rightt.gif")

def run_left():
    global run_x
    global run_y
    run_x=speed_run *-1
    run_y= 0
    run.shape("ufo_left.gif")

def shoot_gun():
    global gun_x, gun_y, shoot, ammo
    if not shoot and game and ammo > 0:
        gun.goto(ch.xcor(), ch.ycor())
        gun_x= ch_x*2
        gun_y= ch_y*2
        shoot = True
        ammo -= 1

def main_game():
    global game
    if not help:
        pen.clear()
        pen_a.clear()
        if not game:
            game = True
            pen_a.write("Time:20  Ammo:5", align="center", font=("Courier", 18, "normal"))
        elif game:
            game = False

def help_menu():
    global help
    if not game and not help:
        wn.bgpic("help.gif")
        pen.clear()
        pen_a.clear()
        run.hideturtle()
        ch.hideturtle()

    if not game and help:
        wn.bgpic("bg.gif")
        run.showturtle()
        ch.showturtle()
        pen.write("Press Enter to Start", align="center", font=("Courier", 36, "normal"))
        pen_a.write("Press 'H' for Help", align="center", font=("Courier", 18, "normal"))

    if help:
        help = False
    else:
        help = True



def reset():
    global s, ammo, game, gun_y, gun_x
    game = False
    gun_x=0
    gun_y=0
    ch.goto(-260, 0)
    run.goto(260, 0)
    gun.goto(400, 0)
    block.goto(-150, 290)
    blocka.goto(0, -290)
    blockb.goto(150, 290)
    ammo = 5
    s=0
    pen_a.clear()
    pen_a.write("Press 'H' for Help", align="center", font=("Courier", 18, "normal"))


# keyboard binding
wn.listen()

wn.onkeypress(ch_up, "w")
wn.onkeypress(ch_down, "s")
wn.onkeypress(ch_right, "d")
wn.onkeypress(ch_left, "a")

wn.onkeypress(shoot_gun, "space")

wn.onkeypress(run_up, "Up")
wn.onkeypress(run_down, "Down")
wn.onkeypress(run_right, "Right")
wn.onkeypress(run_left, "Left")

wn.onkeypress(main_game, "Return")
wn.onkeypress(reset, "r")
wn.onkeypress(help_menu, "h")





while True:
    wn.update()
    while game == True:
        wn.update()
        if block.ycor() < -290:
            block.goto(random.randint(-280, 280), 290)
            s += 1
            p=0.6
            
            

        if blocka.ycor() > 290:
            blocka.goto(random.randint(-280, 280), -290)
            e = random.randint(4, 10)
            e = e / 10

        if blockb.ycor() < -290:
            blockb.goto(random.randint(-280, 280), 290)
            r = random.randint(4, 10)
            r = r / 10

        if (run.xcor() > ch.xcor() - q and run.xcor() < ch.xcor() + q) and (
                run.ycor() > ch.ycor() - q and run.ycor() < ch.ycor() + q):
            pen.write("Runner is Caught!! The Chaser Wins", align="center", font=("Courier", 18, "normal"))
            reset()

        if (block.xcor() > ch.xcor() - q and block.xcor() < ch.xcor() + q) and (
                block.ycor() > ch.ycor() - q and block.ycor() < ch.ycor() + q):
            pen.write("The Chaser got hit. The Runner Wins", align="center", font=("Courier", 18, "normal"))
            reset()

        if (blocka.xcor() > ch.xcor() - q and blocka.xcor() < ch.xcor() + q) and (
                blocka.ycor() > ch.ycor() - q and blocka.ycor() < ch.ycor() + q):
            pen.write("The Chaser got hit. The Runner Wins", align="center", font=("Courier", 18, "normal"))
            reset()

        if (blockb.xcor() > ch.xcor() - q and blockb.xcor() < ch.xcor() + q) and (
                blockb.ycor() > ch.ycor() - q and blockb.ycor() < ch.ycor() + q):
            pen.write("The Chaser got hit. The Runner Wins", align="center", font=("Courier", 18, "normal"))
            reset()

        if (run.xcor() > gun.xcor() - w and run.xcor() < gun.xcor() + w) and (
                gun.ycor() - w < run.ycor() < gun.ycor() + w):
            pen.write("The Runner got hit. The Chaser Wins", align="center", font=("Courier", 18, "normal"))
            reset()

        if s == 20:
            pen.write("Too Slow Chaser!! The Chaser Loss", align="center", font=("Courier", 18, "normal"))
            reset()

    #Blocks movements

        block.sety(block.ycor() - p)
        blocka.sety(blocka.ycor() + e)
        blockb.sety(blockb.ycor() - r)

   #chasers move
        ch.setx(ch.xcor() + ch_x)
        ch.sety(ch.ycor() + ch_y)

    #runners move
        run.setx(run.xcor() + run_x)
        run.sety(run.ycor() + run_y)

    #bullet move
        gun.setx(gun.xcor() + gun_x)
        gun.sety(gun.ycor() + gun_y)

    # border bouncing
        if ch.xcor() > 290 or ch.xcor() < -290:
            ch_x = ch_x * -1
        if ch.ycor() > 290 or ch.ycor() < -290:
            ch_y = ch_y * -1

        if run.xcor() > 290:
            run_left()
        if run.xcor() < -290:
            run_right()
            
        if run.ycor() > 290 or run.ycor() < -290:
            run_y = run_y * -1

    #Shooting
        if (gun.ycor() > 390 or gun.ycor() < -390) or (gun.xcor() > 390 or gun.xcor() < -390):
            shoot = False

        pen_a.clear()
        pen_a.write("Time:{}  Ammo:{}".format(20-s, ammo) , align="center", font=("Courier", 18, "normal"))



    
        
     
        
