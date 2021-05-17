import turtle
import random
#from tkinter import *
import time

print("             **** WELCOME TO TURTLE AND TELEPORTERS ****")

playerprofile1=input("\n-  --------------------------------       Enter Player 1 UserName : ")

def profileCheck(playerprofile,num):
    while True:
        if playerprofile.strip()=="":
            print("X   XXXXXXXXXXXXXXXXXXXXXXXX ENTER A VALID PROFILE NAME XXXXXXXXXXXXXXXXXXXXXXX")
            playerprofile=input("\n-  --------------------------------       Enter Player "+str(num)+" UserName : ")
        else:
            return playerprofile

playerprofile1=profileCheck(playerprofile1,1)

playerprofile2=input("\n-  --------------------------------       Enter Player 2 UserName : ")

playerprofile2=profileCheck(playerprofile2,2)




wn=turtle.Screen()
wn.setup(width=900,height=600)
wn.bgcolor("grey")
wn.title("Turtle & Teleporters")
stx=st1=-300
sty=st2=-250


px=stx+20
py=sty+20

    
    
#player moves
def move(player,pty,r):
    
    x=player.xcor()
    y=player.ycor()
    test=x+(r*50)

    if(test-170<=0):
        player.goto(test,y)
        
    else:
        player.goto(170,y)
        if(y==220):
            player.goto(x,y)
            pty=player.ycor()
        else:
            pty+=50
            player.goto(px+(test-170-50),pty)
    return pty


##switching from points to points

def teleport(p1):
    if (p1.xcor(),p1.ycor()) in start:
        i=start.index((p1.xcor(),p1.ycor()))
        p1.goto(end[i])
    elif(p1.xcor(),p1.ycor()) in end:
        i=end.index((p1.xcor(),p1.ycor()))
        p1.goto(start[i])
    return p1.ycor()


# Vettrathuku
def check(a,b):
    if(a.xcor()==b.xcor() and a.ycor()==b.ycor()):
        b.goto(px,py)

# front page
design=turtle.Turtle()
design.penup()
design.hideturtle()
design.shape("turtle")
design.shapesize(4,4)
design.color("black")

design.goto(-100,100)
design.write("Turtle",font=("Helvetica",50))
time.sleep(0.5)

design.goto(-170,-90)
design.write("Teleporters",font=("Helvetica",50))
time.sleep(0.5)

design.goto(-30,20)
design.color("green")
design.lt(90)
design.showturtle()

time.sleep(3)
design.clear()




# BOARD

# t is the board drawer

t=turtle.Turtle()
t.pensize(5)
t.speed(0)
t.penup()
t.color("white")


for k in range(10):
    for j in range(10):
        t.penup()
        t.goto(st1,st2)
        t.pendown()
        for i in range(4):
            t.fd(50)
            t.lt(90)
        st1+=50
    st2+=50
    st1=stx

time.sleep(1)

t.penup()
t.hideturtle()

t.goto(-400,-250)
t.color("black")
t.write("Start",font=("Helvetica",30))
time.sleep(0.7)

t.goto(220,200)
t.write("End",font=("Helvetica",30))
time.sleep(0.7)

design.hideturtle()

time.sleep(1)


#Random die
    
"""
def spin(clr,r):
    def roll_it():      
        l.config(bg=clr)
        time.sleep(0.5)
        l.config(text=" "+str(r)+" ")
        
    clr=clr
    root=Tk()
    root.title("Die Throw")
    l=Label(root,text="Throw",font=("TimesNewRoman",100))
    l.pack()
    b1=Button(root,text="Rock nd Roll",height=2,width=20,command=roll_it)
    b1.pack()
    #root.bind("<Return>",close)
    root.mainloop()
"""


#teleportation points



start=[]
end=[]

#The 10 points indicates the 100 boxes
#Hint: turtle has the orientation of normal graph with 4 quadrants
points_x=[170,120,70,20,-30,-80,-130,-180,-230,-280]
points_y=[220,170,120,70,20,-30,-80,-130,-180,-230]

def tele_pts(reds,clr,arr):    
    reds.color(clr)
    reds.shape("circle")
    reds.penup()
    
    x=random.randrange(0,len(points_x))
    y=random.randrange(0,len(points_y))
    src=(-280,-230)
    dest=(170,220)

    while (x,y)==src or (x,y)==dest:
        x=random.randrange(0,len(points_x))
        y=random.randrange(0,len(points_y))

    
    reds.goto(points_x[x],points_y[y])
    arr.append((points_x.pop(x),points_y.pop(y)))
    
    

violet1=turtle.Turtle()
violet2=turtle.Turtle()
orange1=turtle.Turtle()
orange2=turtle.Turtle()
green1=turtle.Turtle()
green2=turtle.Turtle()
yellow1=turtle.Turtle()
yellow2=turtle.Turtle()

tele_pts(violet1,"violet",start)
tele_pts(violet2,"violet",end)
tele_pts(orange1,"orange",start)
tele_pts(orange2,"orange",end)
tele_pts(green1,"green",start)
tele_pts(green2,"green",end)
tele_pts(yellow1,"yellow",start)
tele_pts(yellow2,"yellow",end)

time.sleep(2)

#player 1
player1=turtle.Turtle()
player1.pensize(10)
player1.penup()
player1.shape("turtle")
player1.color("blue")
player1.goto(px,py)
player1.penup()
player1.speed(1)
pty1=py



#player 2
player2=turtle.Turtle()
player2.pensize(10)
player2.penup()
player2.shape("turtle")
player2.color("red")
player2.goto(px,py)
player2.penup()
player2.speed(1)
pty2=py


flag=0


#random number for player1
ran1=turtle.Turtle()
ran1.penup()
ran1.hideturtle()
ran1.goto(300,-230)
ran1.color("blue")
ran1.pendown()

#random number for player2
ran2=turtle.Turtle()
ran2.penup()
ran2.hideturtle()
ran2.goto(300,70)
ran2.color("red")
ran2.pendown()


while True:
    ran1.clear()
    r=random.randrange(1,7)
    #spin("red",r)
    ran1.write(" "+str(r)+" ",font=("Helvetica",100))
    time.sleep(1)
    pty1=move(player1,pty1,r)
    check(player1,player2)
    pty1=teleport(player1)
    time.sleep(1)

    if((player1.xcor(),player1.ycor())==(170,220)):
        flag=1
        break
    
    s=random.randrange(1,7)
    
    ran2.clear()
    
    ran2.write(" "+str(s)+" ",font=("Helvetica",100))
    time.sleep(1)
    pty2=move(player2,pty2,s)
    check(player2,player1)
    pty2=teleport(player2)

    
    if((player2.xcor(),player2.ycor())==(170,220)):
        flag=2
        break

# Finishing
t.clear()
violet1.hideturtle()
violet2.hideturtle()
orange1.hideturtle()
orange2.hideturtle()
green1.hideturtle()
green2.hideturtle()
yellow1.hideturtle()
yellow2.hideturtle()
ran1.clear()
ran2.clear()

if(flag==1):
    print("\n\n                             ###################",playerprofile1+" wins ##################")
    
    player2.hideturtle()
    player1.goto(-280,20)
    player1.pendown()
    player1.write(playerprofile1+" Won",font=("Helvetica",50))
    time.sleep(1)
else:
    
    print("\n\n                             ###################",playerprofile2+" wins ##################")
        
    player1.hideturtle()
    player2.goto(-280,20)
    player2.pendown()
    player2.write(playerprofile2+" Won",font=("Helvetica",50))
    time.sleep(1)

