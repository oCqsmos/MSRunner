from tkinter import *
from tkinter import messagebox
import random

def bombClick():
    display=messagebox.showerror("Minesweeper","gameover")
    root.destroy()
    # roo2.destroy()
def numClick(num,pos):
    print("it worked")
    print(num)
    if num==0:
        # tiles[pos[1]][pos[0]]
        tiles[pos[1]][pos[0]].config(command=spake,text=str(num))
        if pos[1]!=len(sweeper):
            tiles[pos[1]+1][pos[0]].invoke()
        if pos[1]!=0:
            tiles[pos[1]-1][pos[0]].invoke()
        if pos[0]!=len(sweeper):
            tiles[pos[1]][pos[0]+1].invoke()
        if pos[1]!=0:
            tiles[pos[1]][pos[0]-1].invoke()
        if pos[1]!=len(sweeper) and pos[0]!=len(sweeper):
            pass
    else:
        tiles[pos[1]][pos[0]].config(command=spake,text=str(num))
def spake():
    pass
        

def gridAdd(kind,gridx,gridy):
    if kind=="bomb":
        # grid[gridy].append(Button(root,text="♦",fg="red"))
        tiles[gridy][gridx]=Button(root,text="♦",fg="red",command=bombClick)
        tiles[gridy][gridx].grid(column=gridx,row=gridy,sticky="NSEW")
    for i in range(0,9):
        if kind==i:
            # grid[gridy].append(Button(root,text=str(i),fg="blue"))
            tiles[gridy][gridx]=Button(root,text='',fg="blue",command=lambda x=i: numClick(x,(gridx,gridy))) 
            tiles[gridy][gridx].grid(column=gridx,row=gridy,sticky="NSEW")


def randomizer(bCount):
    global bPos
    bPos=[]

    xlist=[0,1,2,3,4,5,6,7,8,9]
    ylist=[0,1,2,3,4,5,6,7,8,9]
    for i in range(bCount):
        xt=random.choice(xlist)
        yt=random.choice(ylist)
        xlist.remove(xt)
        ylist.remove(yt)
        bPos.append((xt,yt))
    print(bPos)
    correct=False

    print("AMERICA YA")
    while not correct:
        print("HALLO :D")
        good=0
        for i in bPos:
            if bPos.count(i)>1:
                bPos[bPos.index(i)]=(random.randint(0,10),random.randint(0,10))
            else:
                good+=1
        if good>=bCount-1:
            correct=True

    print(bPos)
randomizer(2)

root = Tk()
root.title('MineSweeper')
for i in range(0,10):
    Grid.rowconfigure(root,i,weight=1)
    Grid.columnconfigure(root,i,weight=1)
# roo2=Tk()
# roo2.title('GameText')

global grid
sweeper=[[0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]]

global tiles
tiles=[[0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]]
textupdates=[]
for i in bPos:
    sweeper[i[0]][i[1]]="hi"
print(sweeper)
top=True
bot=True
rig=True
lef=True
for i in range(0,len(sweeper)):
    for r in range(0,len(sweeper[i])):
        if sweeper[i][r]=="hi":
            pass
        else:
            temp=0
            print(i,r)
            if i!=0:
                top=False
            if i!=len(sweeper)-1:
                bot=False
            if r!=0:
                lef=False
            if r!=len(sweeper[i])-1:
                rig=False


            if not top and not rig:
                if sweeper[i-1][r+1]=="hi":
                    temp+=1
            if not top:
                if sweeper[i-1][r]=="hi":
                    temp+=1
            if not top and not lef:
                if sweeper[i-1][r-1]=="hi":
                    temp+=1
            if not lef:
                if sweeper[i][r-1]=="hi":
                    temp+=1
            if not lef and not bot:
                if sweeper[i+1][r-1]=="hi":
                    temp+=1
            if not bot:
                if sweeper[i+1][r]=="hi":
                    temp+=1
            if not bot and not rig:
                if sweeper[i+1][r+1]=="hi":
                    temp+=1
            if not rig:
                if sweeper[i][r+1]=="hi":
                    temp+=1
            sweeper[i][r]=temp
        
        top=True
        bot=True
        rig=True
        lef=True

print(sweeper)


for i in range(0,len(sweeper)):
    for r in range(0,len(sweeper[i])):
        if sweeper[i][r]=="hi":
            gridAdd("bomb",r,i)
        else:
            for q in range(0,8):
                if sweeper[i][r]==q:
                    gridAdd(q,r,i)

#testing code
# grid[1][5]="abcdefghijklmnopqrstuvwxyz"
# print(grid)
# test=Button(root,text="♦",fg="red")
# test.pack()

root.mainloop()


#button_varialble.configure(text="new text")    use to change the text of a button
# print("hello world")