#include <stdio.h>
#include <string.h>
#define DEBUG 1

// PS. NEVER use gets() in real code.
char * gets ( char * str );

char * pwd = "pwd0";

void print_my_pwd() {
  printf("your pwd is: %s\n", pwd);
}

int check_user(char * uname, char * upwd) {
  char name[12];
  strcpy(name, uname);
  
  if (strcmp(pwd, upwd)) {
    printf("non authorized\n");
    return 1;
  }
  printf("authorized\n");
  print_my_pwd();
  return 0;
}

int main(int argc, char ** argv) {
#ifdef DEBUG
  fprintf(stderr, "%p\n", main);
#endif
  char name[128];
  char pass[128];

  printf("Name? \n");
  gets(name);
  printf("Password? \n");
  gets(pass);
  printf("Hello %s\n", name);
  check_user(name, pass);
  printf("End\n");
  return 0;
}
