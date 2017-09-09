'''Author          Lolmattylol
Creation date   08/09/2017
Verion No       1.01
Contact info    reddit:lolmattylol
if you modify this for the better, please consider sharing with the community over at reddit.com/r/prisonarchitect
Version No     Date of Change   Author          Change
1.00           08/09/2017       lolmattylol     Created first version to prove concept
1.01           09/09/2017       lolmattylol     added DeathRowGUI to create simple graphical user interface
1.02           09/09/2017       lolmattylol     Added option to enter individual prisoner ID
'''
from DeathRow import *
import tkinter
l=["Blue Gang", "Green Gang","Red Gang", "All Gangs", "Gang Leaders","Lieutenants","SuperMax","Legendary","Extreme Traits","Stoical","Fearless","Sentance over 100 yrs","Select Prisoner ID"]
c=["Gang.Id              4","Gang.Id              3","Gang.Id              2","Reputation           GangMember", "Gang.Rank            Leader","Gang.Rank            Lieutenant","Category             SuperMax","Reputation           Legendary","ReputationHigh","Reputation           Stoical","Reputation           Fearless","Served               ","ID"]
root=tkinter.Tk()
Prisons=listPrisons()
PrisonList=[]
IDs=[]
pFileLocation=""
def SelectPrison(p):
    global PrisonList
    global pFileLocation
    for widget in root.winfo_children():
        widget.destroy()
    pFileLocation=userDir+"\\"+p
    PrisonList=file2List(open(pFileLocation,"r"))
    for y in range(0,len(l)-1):
        B=tkinter.Button(root,text=l[y],command=lambda y=y:getIDs(c[y]))
        B.pack()
    B=tkinter.Button(root,text=l[len(l)-1],command=lambda :specificPrisoner(c[len(l)-1]))
    B.pack()
def setID(x,c):
    global IDs
    IDs.append(x)
    getIDs(c)
    
                     
def specificPrisoner(C):
    for widget in root.winfo_children():
        widget.destroy()
    w=tkinter.Label(root,text="Enter Prsioner ID")
    w.pack()
    e=tkinter.Entry(root)
    e.pack()
    b=tkinter.Button(root,text="select",command=lambda : setID(e.get(),C))
    b.pack()

def getIDs(Crit):
    global PrisonList
    global IDs
    global pFileLocation
    for widget in root.winfo_children():
        widget.destroy()
    if Crit!="ID":
        IDs=DeathRowID(PrisonList,Crit)
    deathrowify(IDs,pFileLocation)
    w=tkinter.Label(root,text="A new prison has been created called DeathRow.prison")
    w.pack()
for x in range(0, len(Prisons)):
    a=Prisons[x]
    B=tkinter.Button(root,text=a,command=lambda x=x:SelectPrison(Prisons[x]))
    B.pack()
root.mainloop()
