import tkinter as tk
import customtkinter as ctk
import os
from cryptography.fernet import Fernet

# Documentation
"""
You must have cryptography library alongside with python to make this thing work!
to install Cryptography open terminal and type "pip install cryptography" And thats it!
You can run this code!
"""


def Encrypt():
    
    path=textEntery.get()
    key = Fernet.generate_key()
    print(key)

    if "txt.key" in os.listdir(path):
        print("Key is already present")
        return -1
    
    with open(f"{path}/txt.key", "wb") as txt:
        txt.write(key)
        txt.close()
    files = list(x for x in os.listdir(path) if x !="txt.key")
    print(files)

    # main code
    for file in files:
        with open(f"{path}/{file}", "rb") as TheFile:
            content = TheFile.read()
            TheFile.close()
        contentWithKey = Fernet(key).encrypt(content)
        with open(f"{path}/{file}", "wb") as TheFile:
            TheFile.write(contentWithKey)
            TheFile.close()



def Decrypt():
    
    path=textEntery.get()
    files=list(x for x in os.listdir(path) if x not in ["txt.key"])

    with open(f"{path}/txt.key","rb") as TheKey:
        key=TheKey.read()
        TheKey.close()

    for file in files:
        with open(f"{path}/{file}","rb") as TheFile:
            content=TheFile.read()
            TheFile.close()
        with open(f"{path}/{file}","wb") as TheFile:
            TheFile.write(Fernet(key).decrypt(content))
            TheFile.close()
    os.remove(f"{path}/txt.key")

def status():
    stat="ready!" if textEntery.get() !="" else "Enter a valid path"
    return stat



#########################################gui#########################################
# root
root = tk.Tk()
root.geometry("393x78")
root.title("DE-Encryption")
root.minsize(393,78)
root.maxsize(393,78)
root.configure(bg="black",border=1)

# frame
f1 = tk.Frame(bg="black")
f2=tk.Frame(bg="black")

#Entry
path=tk.StringVar()
textEntery=tk.Entry(f1,textvariable=path, font=("segoeui", 10, "bold"),relief="sunken")

#Text_lables
text = tk.Label(f1, text="Enter your path", font=("segoeui", 10, "bold"), bg="grey",fg="white")
status=tk.Label(f2,text=status(), font=("segoeui", 10, "bold"), bg="green",fg="white",pady=5)


#Button
Encrypt_bt=tk.Button(f1,command=Encrypt,text="Encrypt",bg="red",fg="white",font=("segoeui", 10, "bold"))
Decrypt_bt=tk.Button(f1,command=Decrypt,text="Decrypt",bg="green",fg="white",font=("segoeui", 10, "bold"))

#framepack
f1.pack(side="top",anchor="nw",fill="x")
f2.pack(side="top",fill="x",padx=10,pady=10)

#pack
text.pack(side="left",padx=3)
textEntery.pack(side="left",padx=3)
Encrypt_bt.pack(side="left",padx=3)
Decrypt_bt.pack(side="left",padx=3)
status.pack(fill="x")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.mainloop()
