/* #pragma GCC diagnostic ignored "-Wdeprecated-declarations" */
#include <stdio.h>
#include <pthread.h>
#define DEBUG 1

// PS. NEVER use gets in real code.
char * gets ( char * str );

// Our global data.
pthread_t thread;
pthread_mutex_t mutex;
pthread_cond_t cond;
char mail_body[128];

void init_locks() {
#ifdef DEBUG
  fprintf(stderr, "%p\n", &mutex);
  fprintf(stderr, "%p\n", &cond);
#endif 
  mutex = (pthread_mutex_t)PTHREAD_MUTEX_INITIALIZER;
  cond = (pthread_cond_t)PTHREAD_COND_INITIALIZER;
}

void get_mail() {
  char mail_subject[32];

  // Get email subject and body
  printf("Enter the mail subject:\n");
  gets(mail_subject);
  
  printf("Enter the mail body:\n");
  gets(mail_body);

  return;
}

int main(int argc, char** argv) {
  init_locks();
  get_mail();
  printf("Sending the email\n");
}
