import tkinter as tk
import customtkinter as ctk
import os
from cryptography.fernet import Fernet


# Documentation
"""
You must have cryptography,customtkinter library alongside with python to make this thing work!
to install Cryptography open terminal and type "pip install cryptography" And thats it!
You can run this code!
"""


def Encrypt():
    try:
        path=user_path.get()
        if len(path)<=3:
            status("Enter a valid path","red")
            return 0
        
        key = Fernet.generate_key()
        print(key)
        if "txt.key" in os.listdir(path):
            status("Key is already present!","orange")
            return 0
        
        with open(f"{path}/txt.key", "wb") as txt:
            txt.write(key)
            txt.close()
        os.system(f"attrib +h {path}/txt.key")
        files = list(x for x in os.listdir(path) if x!="txt.key" and os.path.isfile(path+"\\"+x))
        
        #Logic
        for file in files:
            with open(f"{path}/{file}", "rb") as TheFile:
                content = TheFile.read()
                TheFile.close()
            contentWithKey = Fernet(key).encrypt(content)
            with open(f"{path}/{file}", "wb") as TheFile:
                TheFile.write(contentWithKey)
                TheFile.close()
        status("Encryption Complete!","green")

        if OpenFolder_chekbox.get():
            os.startfile(path)
        return 1
    
    except FileNotFoundError as e:
        status("Path not found!","red")
        print(e)
        return 0



def Decrypt():
    try:
        path=user_path.get()
        if len(path)<=3:
            status("Enter a valid path","red")
            return 0
        
        elif "txt.key" not in os.listdir(path):
            status("Key not found","orange")
            return 0
        
        files=list(x for x in os.listdir(path) if  x!="txt.key" and os.path.isfile(path+"\\"+x))
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

        if OpenFolder_chekbox.get():
            os.startfile(path)

        status("Decrypted Sucessfully!","green")
        return 1
    except FileNotFoundError as e:
        status("Path not found!","red")
        print(e)
        return 0
def changeTheme():
    theme=ctk.get_appearance_mode()
    ctk.set_appearance_mode("dark");theme_button.configure(text="Switch Lightmode") if theme=="Light" else ctk.set_appearance_mode("light");theme_button.configure(text="Switch Darkmode")

def status(status,color):
    status_lable.configure(text=status,fg_color=color)



#########################################gui#########################################


root=ctk.CTk()

#geometry
Geometrywidth=500
GeometryHight=250
root.geometry(f"{Geometrywidth}x{GeometryHight}")
root.minsize(Geometrywidth,GeometryHight)
root.maxsize(Geometrywidth,GeometryHight)
root.title("Project-One")

#Default_Arguments
defaulFont=("segoeui",15,"bold")
padX=5
padY=5
defaultCornerRadius=10
defaultWeight=200
defaultHight=40

#theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

#DefaultFrame
f1=ctk.CTkFrame(root,fg_color="transparent",bg_color="transparent",corner_radius=defaultCornerRadius)
f1.pack(padx=padX,pady=padY)

#Changetheme radio button
theme_button=ctk.CTkRadioButton(f1,text="Change Theme",command=changeTheme,font=defaulFont)
theme_button.grid(row=0,column=0,columnspan=2,padx=padX,pady=padY)

#Pathdetails
ctk.CTkLabel(f1,text="Enter path here",font=defaulFont,width=defaultWeight,height=defaultHight).grid(row=1,column=0,padx=padX,pady=padY)
user_path=ctk.StringVar()
ctk.CTkEntry(f1,textvariable=user_path,font=defaulFont,corner_radius=defaultCornerRadius,width=defaultWeight,height=defaultHight).grid(row=1,column=1,padx=padX,pady=padY)

#open folder after complete
openFolder=ctk.BooleanVar()
OpenFolder_chekbox=ctk.CTkCheckBox(f1,text="Open folder after operation?",variable=openFolder,font=defaulFont,corner_radius=6)
OpenFolder_chekbox.grid(row=2,column=0,columnspan=2,padx=padX,pady=padY)

#encrypt button
ctk.CTkButton(f1,command=Encrypt,text="Encrypt",corner_radius=defaultCornerRadius,font=defaulFont,width=defaultWeight,height=defaultHight).grid(row=3,column=0,padx=padX,pady=padY)

#decrypt button
ctk.CTkButton(f1,command=Decrypt,text="Decrypt",corner_radius=defaultCornerRadius,font=defaulFont,width=defaultWeight,height=defaultHight).grid(row=3,column=1,padx=padX,pady=padY)
status_lable=ctk.CTkLabel(f1,text="Loading..",font=defaulFont,corner_radius=defaultCornerRadius,fg_color="orange",text_color="white",width=410,height=defaultHight)
status_lable.grid(row=4,column=0,columnspan=2,padx=padX,pady=padY)

#invoking status
status("Ready!","green")

root.mainloop()
