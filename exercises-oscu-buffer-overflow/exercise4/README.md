# Exercise 4

The application receives two values from the standard input (both terminated by
a newline): (1) mail subject and (2) mail body.

For example:
```
# Compile the program
$ make

$ ./main.elf 
0x55ced147e0c0
0x55ced147e100
Enter the mail subject:
Important message
Enter the mail body:
You won 1000 SEK      
```

Look at the source code, notice that the developer has forgotten to turn off
the `DEBUG` flag (again), causing the program to leak the location of the
global variables `mutex` and `cond` to standard error. Also, note that the
location of variables are also affected by ASLR.

## Problem 4.1

This exercise includes the shell code `shell.py`.  It is generated using `make
shell.bin`, which produce the binary file `shell.bin`. If the shell-code is
executed, it invokes `exec` and execute a `cat` of `/etc/passwd`, revealing the
users of the system.

Forge a subject and e-mail body that make the application to run the above
shell-code.

Since you probably need to produce input that contains "special" bytes, use the
following procedure:

1. complete the python script `solution3.py`, which reads the memory location
   of `mutex` (or `cond`) and then prints the forged output on the standard
   output
2. execute `./solution4.py < my.pipe | ./main.elf 2>my.pipe` (or `make attack`)
   which feeds your `solution4.py` with the `main.elf` standard error output,
   and feeds `main.elf` with the standard output of `solution4.py`.

The target `attack` of the Makefile automates tasks 2, so you only need to
execute `make attack` for step 2.  Your solution consists of the script
`solution4.py`.

To test your solution execute `./test.py`.

## Hints

Debug the program using GDB and find the distance between the location of

1. the variable `mail_subject` and `saved rip`, and 
2. the variable `mutex` (or `cond`) and `mail_body`.

Do not worry if the program crashes after leaking the `passwd` file.

