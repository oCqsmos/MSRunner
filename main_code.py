from tkinter import *
from tkinter import messagebox
import random

def bombClick():
    display=messagebox.showerror("Minesweeper","gameover")
    root.destroy()
    roo2.destroy()
def numClick(num):
    print("it worked")
    print(num)

def gridAdd(kind,gridx,gridy):
    if kind=="bomb":
        # grid[gridy].append(Button(root,text="♦",fg="red"))
        tiles[gridy][gridx]=Button(root,text="♦",fg="red",command=bombClick)
        tiles[gridy][gridx].grid(row=gridx,column=gridy,sticky="NSEW")
    for i in range(0,9):
        if kind==i:
            # grid[gridy].append(Button(root,text=str(i),fg="blue"))
            tiles[gridy][gridx]=Button(root,text=str(i),fg="blue",command=lambda x=i: numClick(x) )
            tiles[gridy][gridx].grid(row=gridx,column=gridy,sticky="NSEW")


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
randomizer(10)

root = Tk()
root.title('MineSweeper')
for i in range(0,10):
    Grid.rowconfigure(root,i,weight=1)
    Grid.columnconfigure(root,i,weight=1)
roo2=Tk()
roo2.title('GameText')

global grid
grid=[[0,0,0,0,0,0,0,0,0,0],
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
    grid[i[0]][i[1]]="hi"
print(grid)
top=True
bot=True
rig=True
lef=True
for i in range(0,len(grid)):
    for r in range(0,len(grid[i])):
        if grid[i][r]=="hi":
            pass
        else:
            temp=0
            print(i,r)
            if i!=0:
                top=False
            if i!=len(grid)-1:
                bot=False
            if r!=0:
                lef=False
            if r!=len(grid[i])-1:
                rig=False


            if not top and not rig:
                if grid[i-1][r+1]=="hi":
                    temp+=1
            if not top:
                if grid[i-1][r]=="hi":
                    temp+=1
            if not top and not lef:
                if grid[i-1][r-1]=="hi":
                    temp+=1
            if not lef:
                if grid[i][r-1]=="hi":
                    temp+=1
            if not lef and not bot:
                if grid[i+1][r-1]=="hi":
                    temp+=1
            if not bot:
                if grid[i+1][r]=="hi":
                    temp+=1
            if not bot and not rig:
                if grid[i+1][r+1]=="hi":
                    temp+=1
            if not rig:
                if grid[i][r+1]=="hi":
                    temp+=1
            grid[i][r]=temp
        
        top=True
        bot=True
        rig=True
        lef=True

print(grid)


for i in range(0,len(grid)):
    for r in range(0,len(grid[i])):
        if grid[i][r]=="hi":
            gridAdd("bomb",r,i)
        else:
            for q in range(0,8):
                if grid[i][r]==q:
                    gridAdd(q,r,i)

#testing code
# grid[1][5]="abcdefghijklmnopqrstuvwxyz"
# print(grid)
# test=Button(root,text="♦",fg="red")
# test.pack()

root.mainloop()


#button_varialble.configure(text="new text")    use to change the text of a button
# print("hello world")