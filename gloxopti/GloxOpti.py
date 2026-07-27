from PIL import Image 

def ImgOpti(filename,extension,level):
    f_file = f"{filename}.{extension}"
    imgopen = Image.open(f_file)
    if extension == "jpeg" or extension == "webp":
        if int(level) == 1:
            imgopen.save(f"opt_{f_file}" , quality=90,optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 2:
            imgopen.save(f"opt_{f_file}" , quality=80,optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 3:
            imgopen.save(f"opt_{f_file}" , quality=70,optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 4:
            imgopen.save(f"opt_{f_file}" , quality=60,optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 5:
            imgopen.save(f"opt_{f_file}" , quality=50,optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        else:
            print("Error Occured : Supported Levels are 1 to 5")
    elif extension == "png":
        if int(level) == 1:
            imgopen.save(f"opt_{f_file}" , compress_level =2 , optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 2:
            imgopen.save(f"opt_{f_file}" , compress_level =2 , optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 3:
            imgopen.save(f"opt_{f_file}" , compress_level =2 , optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 4:
            imgopen.save(f"opt_{f_file}" , compress_level =2 , optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        elif int(level) == 5:
            imgopen.save(f"opt_{f_file}" , compress_level = 9 , optimize = True)
            print("Sucessfully Converted! ~AvgLucer")
        else:
            print("Error Occured : Supported Levels are 1 to 5")
