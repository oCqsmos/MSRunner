from tkinter import *
from tkinter import messagebox
import random
def gridAdd(kind,gridx,gridy):
    if kind=="bomb":
        # grid[gridy].append(Button(root,text="♦",fg="red"))
        grid[gridy][gridx]=Button(root,text="♦",fg="red")
    for i in range(0,8):
        if kind==i:
            # grid[gridy].append(Button(root,text=str(i),fg="blue"))
            grid[gridy][gridx]=Button(root,text=str(i),fg="blue")
def randomizer(bCount):
    bPos=[]

    # correct=False
    # print("AMERICA YA")
    # while not correct:
    #     bPos=[]
    #     for i in range(bCount):
    #         bPos.append((random.randint(0,10),random.randint(0,10)))
    #     good=0
    #     for i in bPos:
    #         if bPos.count(i)==1:
    #             good+=1
    #     if good==10:
    #         correct=True
    #     print("HALLO :D")

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
textupdates=[]

#testing code
# grid[1][5]="abcdefghijklmnopqrstuvwxyz"
# print(grid)
# test=Button(root,text="♦",fg="red")
# test.pack()

root.mainloop()

# print("hello world")