# Exercise 2

The application requires two arguments: (1) a username and (2) a password.
```
Use ./main.elf <user> <password>
```
For example
```
# Compile the program 
$ make

$ ./main.elf roberto 1234
Start
Hello roberto
non authorized
End

$ ./main.elf roberto pwd0
Start
Hello roberto
authorized
End

$ ./main.elf hello pwd0
Start
Hello hello
authorized
End
```

## Problem 2.1
Forge two command line arguments that
allow you to be authenticated
with a wrong password.
Write your solution in the file `solution2.txt`.
For instance, if you used `./main.elf hello 12345`,
then your `solution2.txt` file should look like
```
# exercise 2
# problem 1
# Forge two command line arguments that
# allows you to be authenticated
# with a wrong password.
hello 12345
# end
```

To test your solution execute `./test.py`.

## Hints
Debug the program using GDB. Find the distance between the
locations of the two internal local variables `name` and `pwd`.
