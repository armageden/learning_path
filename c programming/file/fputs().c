#include <stdio.h>
int main() {
  char name[30];
  FILE *file;
  file = fopen("text.txt", "w");
  if (file == NULL) {
    printf("File doesn't exist!");

  } else {
    printf("File is opened\n");
    printf("Enter your name : ");
    gets(name);
    fputs(name, file);
    fputs("\n", file);
    printf("File is written successfully\n");
    fclose(file);
  }
}