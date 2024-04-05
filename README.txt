//topics covered create , open,append , write and delete for a file

A file class with variables name ,content , size ,permission
Methods  - Create read edit delete 

create a file 
x(random variable)= open("name.extension","w" OR "x")

open a file:  //with-to check if resource are correctly handled and cleanup after it is no longer needed.
with open("name.extension","a")
    pass
f.write = to write a file
f.close
"x" = create - create file
"a" = append - make changes to part of it
"w" = write - change the whole thing

remove 
need os import

os.remove("filename")

//topics 

os.path.exist - check for path
os.mkdir - make dir
os.rmdir - remove

//Basic version of the system 
Display option -CORE
    1.Create dir
        a.Write on file
    2.Create file
        a.Choose a dir
            I.if dir not exist call- create dir()
            II.Create 
    3.Append existing file 
    4.remove
        a.remove dir
        b.remove file
//things to Add
1. open a File
2. serach file(file name pattern matching)
3. travsersing directories
4. copy,move file
<--- done till here--->

5. create a zip file
    with password
6.Extracting zip files
    with extract password
7. create archive for zip files
8.check tar file worthy to add 
9.Check for temperoray files and directories


//Additional enhancement
    1.Error Handling:
        if existing directories/files
    2.User Input Validation:
        Validate user inputs for format, forbidden characters.
    3.Improved User Interface:
        Use menus or command-line interface 
    4.Additional File Operations:
        Copy, move, rename, search for files.
    5.Directory Navigation:
        List contents, display current directory.
    6.Persistence:
        Save/load data structures for directory and file management.
    7.User Permissions:
        Implement access control
    8.Documentation and Comments:
        Add comments and documentation to explain code logic.


//Tkinter 
A program is always looping



