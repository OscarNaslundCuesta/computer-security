.PHONY: all attack clean test

all: main.elf shell.bin

main.elf: main.c
	gcc -fno-stack-protector -z execstack -O0  -ggdb -o main.elf main.c

shell.bin: shell.asm
	nasm -f elf64 -o shell.elf shell.asm
	objcopy -O binary shell.elf shell.bin

my.fifo:
	mkfifo my.fifo

attack: main.elf shell.bin my.fifo 
	./solution4.py < my.fifo | ./main.elf 2>my.fifo

test:
	./test.py

clean:
	rm -f *.elf *.bin my.fifo *.out
