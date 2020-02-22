from tkinter import *

import os
import tkinter.filedialog as filedialog

main_window = Tk()
main_window.geometry("550x600")
main_window.configure(background="#02174D")
main_window.title("TOOL BOX")

label_1 = Label(main_window, text="Tool Box", bg="#02174D",fg="#FFF",font=("arial", 35, "bold")).place(x=192, y=85)


def shortcut():
    print("Shortcut Remove")
    # cmd = "attrib -h -r -s /s /d D:\\.............new\\Documents\\Shortcut remover\\files\\*.*- Shortcut"

    p = os.system("attrib -h -r -s /s /d I:\*.*")
    print('p:', p)
    asd = filedialog.askdirectory()
    returned_value = os.system("del " + '"' + asd + "\*.lnk" + '"' + " /f")
    print('returned value:', returned_value)


butn_1 = Button(main_window, text="Shortcut Remove", bg="#4267B0",fg="#FFF", font=("arial", 15, "bold"), borderwidth=3,
                height="2", width="15", command=shortcut).place(x=200, y=170)


def disk_clean():
    print("C Cleaner")

    t = "C:\Windows\Temp"
    tp = "%TEMP%"

    recycleBinEmptyCommand = "rmdir /s %systemdrive%\$Recycle.bin"
    returned_value1 = os.system("del " + '"' + t + '"' + " /f")
    returned_value2 = os.system("del " + '"' + tp + '"' + " /f")
    os.system(recycleBinEmptyCommand)
    print('returned value1:', returned_value1)
    print('returned value2:',returned_value2)


    defragmentation = os.popen("defrag.exe /C").read()
    print("defragmentation:",defragmentation)

    clean = os.popen("cleanmgr.exe /sagerun:1").read()
    print("clean:",clean)

butn_2 = Button(main_window, text="C Cleaner",bg="#313335",fg="#FFF", font=("arial", 15, "bold"), borderwidth=3, height="2",
                width="15", command=disk_clean).place(x=200, y=240)


def registryClear():
    print("Registry Clean")
    asd = "Get-ChildItem -path HKLM:\ -Recurse | where { $_.Name -match 'office12'} | Remove-Item -Force"
    returned_value = os.system(asd)
    print("Registry Cleaning Complete= ", returned_value)


butn_3 = Button(main_window, text="Registery Clean", bg="#313335",fg="#FFF", font=("arial", 15, "bold"), borderwidth=3,
                height="2", width="15", command=registryClear).place(x=200, y=310)


def malware():
    print("Malware Remove")
    p = os.system("attrib -h -r -s /s /d I:\*.*")
    print('p:', p)
    asd = filedialog.askdirectory()
    returned_value = os.system("del " + '"' + asd + "\*.lnk" + "\*.ini" + "\*$Recycle.bin*" '"' + " /f")
    print('returned value:', returned_value)


butn_4 = Button(main_window, text="Malware Remove", bg="#313335",fg="#FFF", font=("arial", 15, "bold"), borderwidth=3, height="2",
                width="15", command=malware).place(x=200, y=380)


def prefetch_file():
    asd = ("C:\WINDOWS\Prefetch")
    returned_value = os.system("del " + '"' + asd + '"' + " /f")
    print("Prefetch Cleaning Complete= ", returned_value)


butn_5 = Button(main_window, text="Prefetch Clean",bg="#4267B0",fg="#FFF", font=("arial", 15, "bold"), borderwidth=3, height="2",
                width="15", command=prefetch_file).place(x=200, y=450)

label_5 = Label(main_window, text="© ARSIT.CO.All copyright reserved.", bg="#02174D",fg="#FFFFFF",font=("italic", 8)).place(x=1, y=580)
main_window.mainloop()
