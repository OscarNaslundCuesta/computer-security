.PHONY: all clean test

DIRS=exercise1 exercise2 exercise3 exercise4

all:
	for ex in $(DIRS); do \
	  make -C $$ex all; \
	done

clean:
	for ex in $(DIRS); do \
	  make -C $$ex clean; \
	done

test:
	for ex in $(DIRS); do \
	  make -C $$ex test; \
	done
