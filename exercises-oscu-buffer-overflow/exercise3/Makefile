.PHONY: all attack clean test

all: main.elf

main.elf: main.c
	gcc -O0 -ggdb -o main.elf main.c -fno-stack-protector

my.fifo:
	mkfifo my.fifo

attack: main.elf my.fifo
	./solution3.py < my.fifo | ./main.elf 2>my.fifo

test:
	./test.py

clean:
	rm -f main.elf my.fifo res.out
