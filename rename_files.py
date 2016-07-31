import os

def rename_files():
    
    #1 - read files from directory.
    file_list = os.listdir("/home/luke/Dropbox/Udacity/ProgrammingFoundationsWithPython/prank")
    print(file_list)
    print("# of files in directory "+str(len(file_list)))
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir("/home/luke/Dropbox/Udacity/ProgrammingFoundationsWithPython/prank")
    print(os.getcwd())
    
    #2 - rename all files in directory.
    for file_name in file_list:
        new_file_name = file_name.translate(None,"0123456789")
        print(file_name+" renamed to "+new_file_name)
        os.rename(file_name, new_file_name)
    os.chdir(saved_path)
    print(os.getcwd())
    print("Program complete.")

rename_files()
