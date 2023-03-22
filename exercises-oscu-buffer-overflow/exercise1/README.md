# Exercise 1

The applications requires two arguments: (1) a username and (2) the
number of chars that should be printed back on screen
```
Use ./main.elf <user> <chars-to-echo>
```
For example
```
# Compile the program
$ make

# Run the program
$ ./main.elf hello 2
Start
Echo he
End

$ ./main.elf hello 5
Start
Echo hello
End
```

## Problem 1.1

Forge two command line arguments that make the application to leak the password
that is stored internally.  Write your solution in the file `solution1.txt`.
For instance, if you used `./main.elf hello 5` to leak the password, then your
`solution1.txt` file should look like
```
# exercise 1
# question 1
# Forge two command line arguments that
# make the application to leak the password that is
# stored internally.
hello 5
# end
```

To test your solution execute `./test.py`.

## Hints
Debug the program using GDB. Find the distance between the
locations of the two internal local variables `name` and `pwd`.
