#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char ** argv) {
  char pwd[8];
  char name[8];
  int i,n = 0;

  printf("Start\n");

  if (argc < 3) {
    printf("Use ./main <user> <chars-to-echo>\n");
    return 1;
  }

  strcpy(pwd, "pwd0");
  strcpy(name, argv[1]);
  n = atoi(argv[2]);

  printf("Echo ");
  for (i=0; i<n; i++) {
    printf("%c", name[i]);
  }
  printf("\n");

  printf("End\n");
  return 0;
}
