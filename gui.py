from Tkinter import *
import math
import random
data=[]
clickStart=0
clickBoxes=0
clickNew=0
def initiate():
	global clickStart
	if clickStart==0:
	    x1 = float(Entry.get(e1))
	    y1 = float(11.5)
	    global xy
	    global initcreds
	    initcreds =x1*y1
	    xy = x1 * y1
	    credits.set(xy)
	    global played
	    played=0
	    clickStart+=1


def clickA():

	global clickBoxes
	global initialChoice
	global remainingChoices
	global shown
	global played
	global newGame
	global clickStart

	if  clickBoxes==clickNew and clickStart==1:

		clickBoxes+=1
		boxA.configure(bg = "red")
		initialChoice=0

		if box_two>box_three:
			C.set(box_three)
			boxC.configure(bg = "blue")
			remainingChoices=[0,1]
			shown=box_three
		elif box_three>box_two:
			B.set(box_two)
			boxB.configure(bg = "blue")
			remainingChoices=[0,2]
			shown=box_two

def clickB():
	global clickBoxes
	global initialChoice
	global remainingChoices
	global shown
	global played
	global newGame
	global clickStart

	if clickBoxes==clickNew and clickStart==1:

		clickBoxes+=1
		boxB.configure(bg = "red")
		initialChoice=1		

		if box_one>box_three:
			C.set(box_three)
			boxC.configure(bg = "blue")
			shown=box_three
			remainingChoices=[1,0]
		elif box_three>box_one:
			A.set(box_one)
			boxA.configure(bg = "blue")
			remainingChoices=[1,2]
			shown=box_one

def clickC():
	global clickBoxes
	global initialChoice
	global remainingChoices
	global shown
	global played
	global clickNew
	global clickStart

	if clickBoxes==clickNew and clickStart==1:

		clickBoxes+=1
		boxC.configure(bg = "red")
		initialChoice=2

		if box_two>box_one:
			A.set(box_one)
			boxA.configure(bg = "blue")
			remainingChoices=[2,1]
			shown=box_one
		elif box_one>box_two:
			B.set(box_two)
			boxBboxC.configure(bg = "blue").configure(bg = "blue")
			remainingChoices=[2,0]
			shown=box_two

def allocate():
	global box_one
	global box_two
	global box_three
	seq=[1,5,15]
	box_one = random.choice(seq)

	if box_one==15:
		seq = [1,5]

	elif box_one==5:
		seq = [1,15]

	else:
		seq = [5,15]

	box_two= random.choice(seq)

	if box_one+box_two==20:
		box_three=1

	elif box_one+box_two==16:
		box_three=5

	else:
		box_three=15

def newGame():
	global clickNew
	global played
	global clickStart
	if clickStart==1 and clickNew==played-1:
		clickNew+=1
		allocate()
		A.set("A")
		B.set("B")
		C.set("C")
		boxA.configure(bg = "white")
		boxB.configure(bg = "white")
		boxC.configure(bg = "white")
		prize.set("0.0")

def howMuchWon(num1):
	global box_one
	global box_two
	global box_three

	if num1==0:
		return box_one

	if num1==1:
		return box_two

	if num1==2:
		return box_three


def functionStick():
	global initialChoice	
	global xy
	global played
	global finalChoice
	global remainingChoices
	global data
	global initcreds
	global clickNew
	global clickBoxes

	if played==clickNew and played==clickBoxes-1:

		played +=1
		gamesplayed.set(played)
		finalChoice=howMuchWon(remainingChoices[0])
		prize.set(finalChoice)

		xy=xy-11.5+finalChoice
		credits.set(xy)

		data.append([played,initialChoice,shown,0,finalChoice,xy-initcreds])

		x1 = float(Entry.get(e1))
		if played>=x1:
			root1.destroy()
	
def functionSwitch():
	global initialChoice
	global xy
	global finalChoice
	global played
	global remainingChoices
	global data
	global initcreds
	global clickNew
	global clickBoxes

	if played==clickNew and played==clickBoxes-1:
		played +=1
		gamesplayed.set(played)

		finalChoice=howMuchWon(remainingChoices[1])
		prize.set(finalChoice)

		xy=xy-11.5+finalChoice
		credits.set(xy)

		data.append([played,initialChoice,shown,1,finalChoice,xy-initcreds])

		x1 = float(Entry.get(e1))
		if played>=x1:
			root1.destroy()

###############################################
allocate()

root1 = Tk()
root1.title("Monty Hall game")
root1.geometry("600x300")


credits=DoubleVar(0)



Label(root1, text="Each game costs 11.5, enter how many games you would like to play and click start").grid(row=0, sticky=W,columnspan=3)
Label(root1, text="Games").grid(row=1, sticky=W)
Label(root1, text="Credits").grid(row=2, sticky=W)

e1 = Entry(root1)
e2 = Entry(root1,textvariable=credits)

start = Button(root1, text='Start',command=initiate)
start.config(height = 2, width=10)
start.grid(row=1, column=4)


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

A=StringVar()
A.set("A")
B=StringVar()
B.set("B")
C=StringVar()
C.set("C")


boxA = Button(root1, textvariable=A,command=clickA)
boxA.config(height = 4, width=8,bg = "white")
boxA.grid(row=7, column=0)
boxB= Button(root1, textvariable=B,command=clickB)
boxB.config(height = 4, width=8,bg = "white")
boxB.grid(row=7, column=1)
boxC = Button(root1, textvariable=C,command=clickC)
boxC.config(height = 4, width=8,bg = "white")
boxC.grid(row=7, column=2)


Label(root1, text="Behind boxes A, B and C are randomly allocated prizes of 1, 5 and 15. Select a box.").grid(row=5, sticky=W,columnspan=3)
Label(root1, text="The dealer will reveal the prize in the box that is the lowest of the two unselected boxes ").grid(row=6, sticky=W,columnspan=3)
Label(root1, text="Would you like to swap your box for the other unopened box?").grid(row=8, sticky=W,columnspan=2)

swap = Button(root1, text='Swap',command=functionSwitch)
swap.config(height = 2, width=10)
swap.grid(row=8, column=2)

stick = Button(root1, text='Stick',command=functionStick)
stick.config(height = 2, width=10)
stick.grid(row=8, column=4)

Label(root1, text="Congratulations, you have won the prize shown:").grid(row=9, sticky=W,columnspan=2)

prize=DoubleVar(0)

e3 = Entry(root1,textvariable=prize)
e3.grid(row=9, column=2)

next = Button(root1, text='Start next game',command=newGame)
next.config(height = 2, width=20)
next.grid(row=10, column=2)

gamesplayed=StringVar()
gamesplayed.set("0")

next = Entry(root1,textvariable=gamesplayed)
next.grid(row=10, column=1)

Label(root1, text="games played so far").grid(row=10, sticky=W)

root1.mainloop()


########################



print data