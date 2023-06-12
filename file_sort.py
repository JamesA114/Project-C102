import os
import shutil

from_dir = "C:/Users/jimmy/Downloads"
to_dir= "C:/Users/jimmy/Desktop/CodingClasses/C102/Stored_documents"

listOfFiles = os.listdir(from_dir)
#print(listOfFiles)
extenList = [ ".txt", '.doc', '.docx', '.pdf']
for file in listOfFiles:
    name, extension = os.path.splitext(file)
    if extension == '':
        continue

    for i in extenList:
        if extension == i:
                path1 = from_dir + '/' + name
                path2 = to_dir + '/' + "Document_Files"
                path3 = to_dir + '/' + "Document_files" + '/' + name

                if os.path.exists(path2):
                    print("Directory Exists...")
                    print("Moving " + name + "....")
                    shutil.move(path1,path3)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + name + "....")
                    shutil.move(path1,path3)

        