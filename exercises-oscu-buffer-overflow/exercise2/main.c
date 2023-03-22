#include <stdio.h>
#include <string.h>

int main(int argc, char ** argv) {
  char pwd[8];
  char name[8];

  if (argc < 3) {
    printf("Use ./main <user> <password>\n");
    return 1;
  }

  printf("Start\n");

  strcpy(pwd, "pwd0");
  strcpy(name, argv[1]);

  printf("Hello %s\n",name);

  if (strcmp(pwd, argv[2]))
    printf("non authorized\n");
  else
    printf("authorized\n");

  printf("End\n");
  return 0;
}
