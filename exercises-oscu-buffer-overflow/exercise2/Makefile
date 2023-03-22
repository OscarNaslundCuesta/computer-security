.PHONY: all clean test

all: main.elf

main.elf: main.c
	gcc -fno-stack-protector -O0 -ggdb -o main.elf main.c

test: main.elf
	./test.py

clean:
	rm -f main.elf
      
