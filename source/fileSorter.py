import os
import shutil
from readSetting import *


folderaddr = input("enter folder path: ")
items = os.listdir(folderaddr)

for i in foldersNeedToCreate:
    if i in items:
        items.remove(i)
    else:
        os.mkdir(folderaddr+"\\"+i)

exceptables = []
exceptableskeys = []
for i in list(settingdatadic.items()):
    # print(i[1])
    for m in i[1]:
        if m == "else":pass
        else:
            exceptables.append(m)
            exceptableskeys.append(i[0])

reverseddic = dict(zip(exceptables,exceptableskeys))

for i in items:
    print(i)
    name, ext = os.path.splitext(i)
    # print(reverseddic)
    if ext == ""or ext ==".text":
        pass
    elif ext in list(reverseddic.keys()):
        print("move to folder "+ reverseddic.get(ext))
        shutil.move(folderaddr + "/" + i, folderaddr + "/"+reverseddic.get(ext)+"/" + i)
    else: 
        print("move to docs")
        shutil.move(folderaddr + "/" + i, folderaddr + "/documents/" + i)

print("─────────────────────────────────────────────────────────────────────────────────────────────────────────")
print("Done!")
print("─────────────────────────────────────────────────────────────────────────────────────────────────────────")
print("Made By Tank Sman \nTelegram :")
print("   __                             __   __                     __")
print("  / /_      ____ ___   ___      _/_/  / /_  ____ _   ____    / /__   _____   ____ ___   ____ _   ____")
print(" / __/     / __ `__ \ / _ \   _/_/   / __/ / __ `/  / __ \  / //_/  / ___/  / __ `__ \ / __ `/  / __ \\")
print("/ /_   _  / / / / / //  __/ _/_/    / /_  / /_/ /  / / / / / ,<    (__  )  / / / / / // /_/ /  / / / /")
print("\__/  (_)/_/ /_/ /_/ \___/ /_/      \__/  \__,_/  /_/ /_/ /_/|_|  /____/  /_/ /_/ /_/ \__,_/  /_/ /_/")
# print(art.text2art("t.me/tanksman",font="slant"))
print("─────────────────────────────────────────────────────────────────────────────────────────────────────────")
input("press enter to exit.")