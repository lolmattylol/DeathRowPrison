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

