#  NAME

**AirBnB clone**, Our own version of a Airbnb.


# SYNOPSIS

**./console.py**


# DESCRIPTION

When you run the./console.py console on a terminal, A prompt (hbnb) will apear on your screem, in where you can type your command and when you hit enter it will run the command and do that you ask for displaying the output on the stdout(Standar Output) then it will be waiting for you to enter another command, all of this in interacive mode. But also it have a non-interactive mode in where you just tell what command to execute, it will run it. but it wont wait for your to enter more commands.


# EXAMPLE

This **AirBnb clone** works like this:
On **non-interactive mode:**
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$


On **interactive mode:**
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$


# FILES

-   **README** This file have a description of the project, how to start it and how to use the command interpreter.

-   **AUTHORS** This the the file that contains the authors of the proyect.
-   **BaseModel.py** This is the file that contains the class BaseModel that defines attributes/methods for other classes.
-   **Unittests** The folder tests files that contains tests with will tell us if the code works. 
-   **console.py** This file "console.py" contains the entry point of one command interpreter
-   **user.py** This file contains the class User that inherits from BaseModel and adds somenew attributes/methods.
-   **file_storage.py** This file contains a instance call FileStorage, it funtion is to manage correctly serialization and deserialization of almost all of our class, and will soport changes to works with all of the new classes.


# AUTHOR
AirBnB Clone project for Holberton School by Michelle Molina, Felipe Prado.