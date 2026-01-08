import os

import shutil

print("File Organiser")

folder_path =input("Enter the folder path:")
files =os.listdir(folder_path)

print(files)

choice =input("Proceed with file rearrangement:(yes/no)?  ")

if "yes"== choice.lower():

    for file in files:
        full_path =os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            extention =os.path.splitext(file)
            print(f"\n{file} ({extention[1]})")

            if extention[1] == "":
                continue

            folder_extention_name =str(extention[1][1:])
            path1= os.path.join(folder_path,folder_extention_name)
            
            if os.path.exists(path1):
                print( f"Folder exist for {extention[1][1:]}")

            else:
                folder_extention =os.makedirs(path1)
                print( f"Folder {folder_extention_name} made")

            destination_path =os.path.join(path1, file)
            shutil.move(full_path , destination_path) 


elif "no"== choice.lower():
    print("Avoiding file rearrangement")
                          
else:
    print("Enter a valid choice.")

