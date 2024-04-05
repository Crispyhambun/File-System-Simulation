import os
import fnmatch as fn
import shutil as sh
import zipfile as zip
class file_Management():   
    def open_file(self):
        Dir_path = dir_mn.check_dir()
        if Dir_path:
            F_name=input("Enter the name of the file")
            try:
                file_Path = os.path.join(Dir_path,F_name)
                with open(file_Path,"x") as f:
                       open_f = f.read()
                       return open_f
            except FileNotFoundError:
                 print(f"file {F_name} not found ")
    def create_File(self):
        Dir_path = dir_mn.check_dir()
        try:
            if Dir_path:
                F_name=input("Enter the name of the file")
                if not F_name:
                    print("file must have name")
                try:
                    file_path = os.path.join(Dir_path,F_name)
                    with open (file_path,'x') as new_file:
                        print("File '{F_name}.txt'  created Successfully")
                except FileExistsError:
                    print(f"File '{F_name}.txt' already Exists")
        except FileNotFoundError:
                print("Invalid Path ",Dir_path)
    def delete_File(self):
        Dir_path = dir_mn.check_dir()
        if Dir_path:
            try:
                F_name=input("Enter file name")
                file_Path = os.path.join(Dir_path,F_name)
                if os.path.exists(file_Path):
                    os.remove(file_Path)
                    print("Removed file successfully")
            except FileNotFoundError as e:
                print("Invalid or missing directories",e)
    def search_File(self):
        Dir_path = dir_mn.check_dir()
        if Dir_path:
            F_name=input("Enter the name of the file")
            match_files =[]
            try:
                for F_name in os.listdir(Dir_path):
                    if fn.fnmatch(F_name,'*.txt'):
                        match_files.append(F_name)
                return match_files
            except FileNotFoundError:
                 print(f"File '{F_name}.txt' does not exist ")              
class directory_Management():
    def check_dir(self):
        Dir_path = input("Enter the path of the directory")
        if not os.path.exists(Dir_path):
            Exit = int(input("Few directories missing do you want to create them \n1.Yes\n2.No?"))
            try:
                if Exit==1:
                    print("Created the directory and other missing directories")
                    os.makedirs(Dir_path) 
                    return True
            except FileNotFoundError as e :
                print("File not fond", str(e))
                return False
        else:
            return Dir_path
    def remove_Path(self):
            Dir_path = self.check_dir()
            try:
                if Dir_path:
                    os.rmdir(Dir_path)
                    print("Removed Directory successfully")
            except FileNotFoundError as e:
                    print("Invalid or missing directories",e)
    def list_Directories(self):
        Dir_path = self.check_dir()
        if Dir_path:
            try:
                   directories = [d for d in os.listdir(Dir_path) if os.path.join(Dir_path,d) ]
                   return directories
            except FileNotFoundError:
                 print(f"{Dir_path} is invalid")
        else:
             print(f"{Dir_path} is invalid")
class file_Operations():
    def write_File(self):
        Dir_path = dir_mn.check_dir()
        F_name=input("Enter the name of the file")
        try:
            file_Path = os.path.join(Dir_path,F_name)
            with open(file_Path,"a") as Uappend:
                    changes =input("Enter data to change")
                    Uappend.write(changes)
        except FileNotFoundError as e:
               print("No such file exists!!",e)
    def copy_File(self):
        F_name = input("Enter the name File to be copied ")
        file_Path= dir_mn.check_dir()
        try:
            src = os.path.join(file_Path,F_name)
        except FileNotFoundError:
            print("Error")
        print("Enter the File where it has to be copied")
        dst= dir_mn.check_dir()
        try:
            if src and dst:
                sh.copy(src,dst)
                print(f"File '{src}' copied to '{dst}' successfully.")
        except PermissionError:
            print("Error: Insufficient permissions to copy the file.")
        except sh.SameFileError:
            print("Error: Source and destination paths point to the same file.")
        except IOError as e:
            print(f"IO Error: {e}")
    def move_File(self):
        F_name = input("Enter the name File to be Moved ")
        file_Path= dir_mn.check_dir()
        try:
            src = os.path.join(file_Path,F_name)
        except FileNotFoundError:
            print("Error")
        print("Enter the File where it has to be Moved")
        dst= dir_mn.check_dir()
        try:
            if src and dst:
                sh.move(src,dst)
                print(f"File '{src}' Moved to '{dst}' successfully.")
        except PermissionError:
            print("Error: Insufficient permissions to copy the file.")
        except sh.SameFileError:
            print("Error: Source and destination paths point to the same file.")
        except IOError as e:
            print(f"IO Error: {e}")
class add_Function():
    def create_Zip(self):
        Dir_path = dir_mn.check_dir()
        try:
            if Dir_path:
                zip_Archive = [d for d in os.listdir(Dir_path) if os.path.join(Dir_path,d) ]
                
                zip_Name = input("Enter the Name of the Archive")
                with zip.ZipFile(zip_Name,'.zip','w') as zip_File:
                    for file in zip_Archive:
                       new_Zip = zip_File.write(file,os.path.basename(file))
                with zip.ZipFiel(zip) as zi:
                    print(f"Archive '{zip_Name}.zip' made sucessfully")
            
        except FileNotFoundError:
            print("Error")
dir_mn = directory_Management()
cf = file_Management()
foper = file_Operations()
foper.copy_File()