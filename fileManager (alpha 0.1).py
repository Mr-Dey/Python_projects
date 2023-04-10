import os
import datetime
import shutil


# mover method
def mover(dir):
    photos = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"]
    videos = [".mp4", ".avi", ".flv", ".wmv", ".mov", ".mkv",
              ".webm", ".mpeg", ".mpg", ".3gp", ".m4v", ".rm", ".swf", ".vob"]

    # for photos
    for z in os.listdir(dir):
        name, ext = os.path.splitext(z)
        if ext in photos:
            if "photos" not in os.listdir(dir):
                os.mkdir(dir+"\\photos")
                print("Photos folder created")
            try:
                shutil.move(os.path.join(dir, z), dir+"\\photos")
            except:
                FileExistsError
                date = datetime.datetime.now()
                date = date.strftime("%Y-%m-%d-%H-%M-%S")
                os.rename(dir+"\\"+z, dir+"\\"+name+date+ext)
                mover(dir)


# main method
def main():
    default_path = f"C:\\Users\\{os.getlogin()}\\Downloads"
    source_dir = default_path
    user_inp = input(
        "Enter file path or press [1] for default folder(default is download folder)\n-->")
    if user_inp != "1":
        user_inp = user_inp.replace("\\", "\\\\")
        source_dir = user_inp
    mover(source_dir)


if __name__ == "__main__":
    main()
