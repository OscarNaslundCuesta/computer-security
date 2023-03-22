# Exercise 3

The application receives two values from the standard input (both terminated by
a newline): (1) name and (2) password.

For example:
```
# Compile the program
$ make

$ ./main.elf 
0x56ff2531280
Start
Name? 
student
Password?
time2work
Hello student
non authorized
End

$ ./main.elf
0x55ff2198280
Start
Name?
student
Password?
pwd0
Hello student
authorized
End

$ ./main.elf hello pwd0
0x55b00654c280
Start
Name?
hello
Password?
pwd0
Hello hello 
authorized
End
```

Look at the source code, notice that the developer has forgotten to turn off
the `DEBUG` flag, causing the program to leak the location of the main
function to standard error. Also, notice that the location of the main function
changes on every execution due to ASLR.

## Problem 3.1
Forge a username that makes the application leak the password that is stored
internally.

Since you probably need a username that contains "special" bytes, use the
following procedure:

1. complete the python script `solution3.py`, which reads the memory location
   of main and then prints the forged output on the standard output
2. execute `./solution3.py < my.pipe | ./main.elf 2>my.pipe` which feeds your
   `solution3.py` with the `main.elf` standard error output, and feeds
   `main.elf` with the standard output of `solution3.py`.

The target `attack` of the Makefile automates tasks 2, so you only need to execute `make attack` for step 2.  Your solution consists of the script `solution3.py`.

To test your solution execute `./test.py`.

## Hints
Debug the program using GDB and find the distance between the location of
1. the variable `name` and `saved rip`, and 
2. the function `main` and `print_my_pwd`.

Do not worry if the program crashes after leaking the password.

