import os
import shutil
from readSetting import *
from tkinter import *

tk=Tk()
tk.configure(background='#666666')
path=StringVar(tk)

tk.title("File Sorter")
tk.geometry("600x600")
# folderaddr = input("enter folder path: ")
def run():
    folderaddr=path.get()
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
            print("moving to  folder "+ reverseddic.get(ext))
            print()
            shutil.move(folderaddr + "/" + i, folderaddr + "/"+reverseddic.get(ext)+"/" + i)
        else: 
            print("moveing file to docs")
            print()
            shutil.move(folderaddr + "/" + i, folderaddr + "/documents/" + i)
    unname=Label(tk,text="Done!")
    unname.configure(background='#666666',fg="#eeeeee",font=('sans-serif', 15))
    unname.pack()

# print("─────────────────────────────────────────────────────────────────────────────────────────────────────────")
t1=Label(tk,text="path of folder:")
t1.configure(background='#666666',fg="#eeeeee",font=('sans-serif', 24))
t1.pack()
E1=Entry(tk,textvariable=path,width=50)
E1.configure(background='#888888',fg="#eeeeee",font=('sans-serif', 15))
E1.pack()
b1=Button(tk,text="Run!",command=run)
b1.configure(background='#777777',fg="#eeeeee",font=('sans-serif', 17))
b1.pack()
# print("─────────────────────────────────────────────────────────────────────────────────────────────────────────")
print("Done!")
tk.mainloop()
print("─────────────────────────────────────────────────────────────────────────────────────────────────────────")
print("Made By Tank Sman \nTelegram :")
print("   __                             __   __                     __")
print("  / /_      ____ ___   ___      _/_/  / /_  ____ _   ____    / /__   _____   ____ ___   ____ _   ____")
print(" / __/     / __ `__ \ / _ \   _/_/   / __/ / __ `/  / __ \  / //_/  / ___/  / __ `__ \ / __ `/  / __ \\")
print("/ /_   _  / / / / / //  __/ _/_/    / /_  / /_/ /  / / / / / ,<    (__  )  / / / / / // /_/ /  / / / /")
print("\__/  (_)/_/ /_/ /_/ \___/ /_/      \__/  \__,_/  /_/ /_/ /_/|_|  /____/  /_/ /_/ /_/ \__,_/  /_/ /_/")
print("─────────────────────────────────────────────────────────────────────────────────────────────────────────")
# print(art.text2art("t.me/tanksman",font="slant"))
# input("press enter to exit.")
# auto-py-to-exe