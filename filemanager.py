import os
import shutil

def filemanager(path):
    #creat a list of directoy as per required if not exist
    x = ["pdf","compressed","photos","programs","excel","word","ppt","text","video","music","font","Photoshop","other"]

    #for loop using try except method to make multiplae folder/dirctory
    for z in x:
        try:
            os.mkdir(path+"\\"+z)
        except(FileExistsError):
            pass

    #move file's to mentioned directory
    for f in os.listdir(path):
        filename, file_ext = os.path.splitext(f)
        try:
            if not file_ext:
                pass
            elif file_ext in ('.pdf',".PDF"):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"pdf",f'{filename}{file_ext}'))
            
            elif file_ext in ('.mp3'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"music",f'{filename}{file_ext}'))

            elif file_ext in ('.zip','.rar','.gz','.img','.iso','.ISO'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"compressed",f'{filename}{file_ext}'))
            
            elif file_ext in ('.jpg','.png','.jpeg'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"photos",f'{filename}{file_ext}'))
            
            elif file_ext in ('.exe','.EXE','.msi','.application',".Appx"):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"programs",f'{filename}{file_ext}'))
            
        
            elif file_ext in ('.xlsx','.cvs','.xls'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"excel",f'{filename}{file_ext}'))
            
            elif file_ext in ('.docx'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"word",f'{filename}{file_ext}'))
            
            elif file_ext in ('.pptx',".ppt"):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"ppt",f'{filename}{file_ext}'))
                    
            elif file_ext in (".psd"):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"Photoshop",f'{filename}{file_ext}'))

            elif file_ext in ('.txt'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"text",f'{filename}{file_ext}'))
            
            elif file_ext in ('.mkv','.mp4','.avi','.wmv'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"video",f'{filename}{file_ext}'))

            elif file_ext in ('.ttf','.otf'):
                shutil.move(
                    os.path.join(path, f'{filename}{file_ext}'),
                    os.path.join(path,"font",f'{filename}{file_ext}'))
            
            elif file_ext in (".bat",".py"):
                pass
            
        except (FileNotFoundError, PermissionError,FileExistsError):
            pass
    print("Sucessfull!")


path0=input("Whats the path??\n==>>")
filemanager(path0)