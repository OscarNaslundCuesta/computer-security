/* #pragma GCC diagnostic ignored "-Wdeprecated-declarations" */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char global_var[16];

void afunction(char * username) {
  char local_var[16];
  strcpy(local_var, username);
  scanf("%s", global_var);

  printf("User %s has password %s\n", local_var, global_var);
}

int main(int argc, char** argv) {

  if (argc < 2) {
    printf("Use ./main <username>\n<input password>\n");
    return 0;
  }

  afunction(argv[1]);
  return 0;
}
