import os
from cryptography.fernet import Fernet


#Documentation
"""
You must have cryptography library alongside with python to make this thing work!
to install Cryptography open terminal and type "pip install cryptography" And thats it!
You can run this code!
"""

def main():
    for x in range(5):
        EncryptOrDecrypt=input("Press (E) for encrypt and (D) for Decrypt.\n->>").lower()
        if EncryptOrDecrypt=="e":
            path=input("Enter your path!\n->>")
            Encrypt(path)
            break
        elif EncryptOrDecrypt=="d":
            path=input("Enter your path!\n->>")
            Decrypt(path)
            break
        else:
            print("Try again!")
            continue
    print("Program Closed!")


def Encrypt(path):
    key=Fernet.generate_key()
    print(key)

    with open(f"{path}/txt.key","wb") as txt:
        txt.write(key)
        txt.close()
    files=list(x for x in os.listdir(path) if x not in ["Try.py","txt.key"])
    print(files)
    
    #main code
    for file in files:
        with open(f"{path}/{file}","rb") as TheFile:
            content=TheFile.read()
            TheFile.close()
        contentWithKey=Fernet(key).encrypt(content)
        with open(f"{path}/{file}","wb") as TheFile:
            TheFile.write(contentWithKey)
            TheFile.close()

def Decrypt(path):
    files=list(x for x in os.listdir(path) if x not in ["txt.key","Try.py"])

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


main()