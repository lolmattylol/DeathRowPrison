#Author          Lolmattylol
#Creation date   08/09/2017
#Verion No       1.00
#Contact info    reddit:lolmattylol
#if you modify this for the better, please consider sharing with the community over at reddit.com/r/prisonarchitect
import os
from pathlib import Path
from os import walk
userDir=str(Path.home())+"\AppData\Local\Introversion\Prison Architect\saves"
def listPrisons():
    Prisons=[]
    for (dirpath, dirnames, filenames) in walk(userDir):
         for item in filenames:
             if ".prison" in item:
                 Prisons.append(item)
    return Prisons
def selectPrison(p):
    x=0
    for item in p:
        x+=1
        print (x,item)
    selected=int(input("Please enter the number prison you would like to edit\n"))
    return p[selected-1]
def file2List(f):
    listy=[]
    for line in f:
        listy.append(line)
    return listy
def DeathRowID(l,criteria):
    ID=[]
    prisoner=""
    for i in range(0,len(l)):
        if "Id.i" in l[i]:
            if "Type                 Prisoner" in l[i+2]:
                prisoner=(l[i][29:].strip())
        if criteria in l[i]:
            if criteria == "Served               ":
                s=(l[i-1][33:].strip())
                if int(s)>100:
                    ID.append(prisoner)
            else:
                ID.append(prisoner)
    return ID
def getCrit():
    l=["Blue Gang", "Green Gang","Red Gang", "All Gangs", "Gang Leaders","Lieutenants","SuperMax","Legendary","Extreme Traits"
       ,"Stoical","Fearless","Sentance over 100 yrs"]
    c=["Gang.Id              4","Gang.Id              3","Gang.Id              2","Reputation           GangMember",
       "Gang.Rank            Leader","Gang.Rank            Lieutenant","Category             SuperMax",
       "Reputation           Legendary","ReputationHigh","Reputation           Stoical","Reputation           Fearless","Served               "]
    print("Select the criteria for death row inmates")
    for i in range(0, len(l)):
        print(i+1,l[i])
    return(c[int(input())-1])
        
def deathrowify(l,f):
    x=open(f,"r")
    y=open(userDir+"//DeathROW.prison","w")
    prisoner=False
    for line in x:
        for i in l:
            if ("Id.i                 "+i) in line:
                prisoner=True
                l.remove(i)
        if prisoner==True:
            if "END" in line:
                prisoner=False
                y.write(line)
            elif "Category" in line:
                y.write("        Category             DeathRow  \n")
                y.write("		ClemencyChance       0.05\n")
            else:
                y.write(line)
        else:
            y.write(line)
    y.close()
        



def main():
    prison=listPrisons()
    pFileLocation=userDir+"\\"+selectPrison(prison)
    PrisonList=file2List(open(pFileLocation,"r"))
    Criteria=getCrit()
    IDs=DeathRowID(PrisonList,Criteria)
    deathrowify(IDs,pFileLocation)
main()
