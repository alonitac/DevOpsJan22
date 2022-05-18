#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

struct stat st = {0};



int main() {
    if (stat("./welcomeToDevOpsJan22", &st) == -1) {
      mkdir("./welcomeToDevOpsJan22", 0700);
    }

    int num;
    FILE *fptr;

    // use appropriate location if you are using MacOS or Linux
    fptr = fopen("welcomeToDevOpsJan22/goodLuck","w");

    if(fptr == NULL)
    {
    printf("Error!");
    exit(1);
    }

    fprintf(fptr,"%s","There you go... tell me what I do...");
    fclose(fptr);
  return 0;
}