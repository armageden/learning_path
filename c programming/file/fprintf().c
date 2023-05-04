#include <stdio.h>
int main() {
  char name[30];
  int age;
  FILE *file;
  file = fopen("text.txt", "a");
  if (file == NULL) {
    printf("File doesn't exist!");

  } else {
    printf("File is opened\n");
    printf("Enter your name : ");
    gets(name);
    printf("Enter your age : ");
    scanf("%d",&age);
    fprintf(file, "Name : %s , Age : %d\n",name,age);
    printf("File is written successfully\n");
    fclose(file);
  }
}