#Author          Lolmattylol
#Creation date   08/09/2017
#Verion No       1.01
#Contact info    reddit:lolmattylol
#if you modify this for the better, please consider sharing with the community over at reddit.com/r/prisonarchitect
#Version No     Date of Change  Author          Change
#1.00           08/09/2017      lolmattylol     Created first version to prove concept
#1.01           09/09/2017      lolmattylol     added DeathRowGUI to create simple graphical user interface

from DeathRow import *
import tkinter
l=["Blue Gang", "Green Gang","Red Gang", "All Gangs", "Gang Leaders","Lieutenants","SuperMax","Legendary","Extreme Traits","Stoical","Fearless","Sentance over 100 yrs"]
c=["Gang.Id              4","Gang.Id              3","Gang.Id              2","Reputation           GangMember", "Gang.Rank            Leader","Gang.Rank            Lieutenant","Category             SuperMax","Reputation           Legendary","ReputationHigh","Reputation           Stoical","Reputation           Fearless","Served               "]
root=tkinter.Tk()
Prisons=listPrisons()
PrisonList=[]
def SelectPrison(p):
    for widget in root.winfo_children():
        widget.destroy()
    pFileLocation=userDir+"\\"+p
    PrisonList=file2List(open(pFileLocation,"r"))
    for y in range(0,len(l)):
        B=tkinter.Button(root,text=l[y],command=lambda y=y:getIDs(PrisonList,c[y],pFileLocation))
        B.pack()
def getIDs(PL,Crit,f):
    IDs=DeathRowID(PL,Crit)
    deathrowify(IDs,f)
    for widget in root.winfo_children():
        widget.destroy()
    w=tkinter.Label(root,text="A new prison has been created called DeathRow.prison")
    w.pack()
for x in range(0, len(Prisons)):
    a=Prisons[x]
    B=tkinter.Button(root,text=a,command=lambda x=x:SelectPrison(Prisons[x]))
    B.pack()
root.mainloop()
