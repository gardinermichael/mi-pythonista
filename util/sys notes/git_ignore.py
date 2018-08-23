#  Aug 23, 2018 at 9:20 AM

# https://blog.gitprime.com/a-practical-guide-to-using-gitignore/
# https://www.gitignore.io/
# https://www.gitignore.io/api/python


If we wanted to exclude the file, “example.txt”, we would simply create a file, “.gitignore”, containing this line:
	
example.txt

Easy, right? If we wanted to exclude all text files, we would simply add the line:
	
*.txt

__________________________________________________

Put .gitignore in the working directory. It doesn't work if you put it in the .git (repository) directory.

$ ls -1d .git*
.git
.gitignore

______________

f you want to do it globally, you can use the default path git will search for. just place it inside a file named "ignore" in the path "~/.config/git"

(so full path for your file is: ~/.config/git/ignore)

_______________

As the other answers stated, you can place .gitignore within any directory in a Git repository. However, if you need to have a private version of .gitignore, you can add the rules to .git/info/exclude file.
__________________________________________________


how to write a line in a gitignore?

These simple rule can make it easier to read and avoid name collision

if it's a folder, add a final /
if it's at the root folder, add a starting /
if it's a sub-file or sub-folder add a starting */
if you want to create an exception, add a starting !
Examples:

/dist/ (root folder)
/node_modules/ (root folder)
*.pyc (any file anywhere with .pyc extension)
__pycache__/ (any folder anywhere with that name)


Understanding gitignore locations

There are (more than) 3 possible locations where to ignore a file/folder for git:

~/.gitignore
.gitignore in the project's folder
.git/info/exclude in the project's folder
home gitignore

is located in ~/.gitignore and contains anything that is specific to you like your OS files, your editors files, etc.

.DS_Store if you're on a MacBook
Thumbs.db is you're on Windows
your favorite code editors files / folders (.atom, .idea/, .project, *.sublime-workspace, …)
Globally anything that will be common to multiple projects in a different language should probably be here.

Project's gitignore

Here you should insert anything that is specific to the nature of your project, like *.pyc for python 2, __pycache__/ for python 3, /node_modules/ for npm projects, …

Project's .git/info/exclude

for ignoring files and folders that are specific to your project and to your preferences or environment. In other words, this location is to common point between your home gitignore and your project's gitignore. It is less common to use this though.

Examples for python: /env/, /venv/

http://vinyll.scopyleft.fr/using-gitignore-the-right-way/

__________________________________________________

# page title: Some common .gitignore configurations
# url: https://gist.github.com/octocat/9257657

# filename >>> .gitignore
# Compiled source #
###################
*.com
*.class
*.dll
*.exe
*.o
*.so

# Packages #
############
# it's better to unpack these files and commit the raw source
# git has its own built in compression methods
*.7z
*.dmg
*.gz
*.iso
*.jar
*.rar
*.tar
*.zip

# Logs and databases #
######################
*.log
*.sql
*.sqlite

# OS generated files #
######################
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
