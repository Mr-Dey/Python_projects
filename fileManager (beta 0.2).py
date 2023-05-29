import os
import datetime
import shutil


# logic
def logic(dir):
    photos = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"]
    videos = [".mp4", ".avi", ".flv", ".wmv", ".mov", ".mkv",
              ".webm", ".mpeg", ".mpg", ".3gp", ".m4v", ".rm", ".swf", ".vob"]
    compressed = ['.zip', '.rar', '.gz', '.tar', '.7z',
                  '.bz2', '.xz', '.tar.gz', '.tar.xz', '.tar.bz2']
    pdf = ['.pdf', '.PDF']
    word = ['.doc', '.docx', '.docm', '.dot', '.dotx', '.dotm']
    excel = ['.xls', '.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm']
    program = ['.exe', '.msi', '.com', '.bat', '.cmd', '.scr', '.cpl', '.hta']
    text = [".txt", ".csv", ".tsv", ".log", ".json", ".xml", ".html", ".htm", ".md", ".py", ".cpp", ".java", ".c", ".h",
            ".php", ".rb", ".pl", ".sql", ".css", ".js", ".yaml", ".ini", ".cfg", ".bat", ".sh", ".tex", ".rtf", ".doc", ".docx"]
    ppt = [".ppt",".pptx",".pps",".ppsx",".pot",".potx",".odp"]


    fileDict = {x: f"photos" for x in photos}
    fileDict.update({x: f"videos" for x in videos})
    fileDict.update({x: f"compressed" for x in compressed})
    fileDict.update({x: f"pdf" for x in pdf})
    fileDict.update({x: f"word" for x in word})
    fileDict.update({x: f"program" for x in program})
    fileDict.update({x: f"excel" for x in excel})
    fileDict.update({x: f"text" for x in text})
    fileDict.update({x: f"ppt" for x in ppt})

    for z in os.listdir(dir):
        name, ext = os.path.splitext(z)
        ext = ext.lower()
        if ext in fileDict.keys():
            if fileDict[ext] not in os.listdir(dir):
                os.mkdir(dir+f"/{fileDict[ext]}")
                print(f"{fileDict[ext]} folder created.")
            try:
                shutil.move(os.path.join(dir, z), dir+f"/{fileDict[ext]}")
            except:
                FileExistsError
                date = datetime.datetime.now()
                date = date.strftime("%Y-%m-%d-%H-%M-%S")
                os.rename(dir+"/"+z, dir+"/"+name+date+ext)
                logic(dir)


# main function
def main():
    default_path = f"C:/Users/{os.getlogin()}/Downloads"
    source_dir = default_path
    user_inp = input(
        "Enter file path or press [1] for default folder(default is download folder)\n-->")
    if user_inp != "1":
        user_inp = user_inp.replace("\\", "/")
        source_dir = user_inp
    logic(source_dir)


if __name__ == "__main__":
    main()
