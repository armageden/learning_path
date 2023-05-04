#include <stdio.h>
int main() {

  FILE *file;
  char name[30];
  int i, num, age, phone_number;
  file = fopen("Student detail.txt", "a");
  if (file == NULL) {
    printf("The file doesn't exist!\n");
  } else {
    printf("The file is opened!\n");
    printf("Enter the number of students : ");
    scanf("%d", &num);
    for (i = 1; i <= num; i++) {
      printf("Enter Student Name : ");
      scanf("%s",&name);
      printf("Enter student age : ");
      scanf("%d", &age);
      printf("Enter student phone-number : ");
      scanf("%d", &phone_number);
      fprintf(file, "%s\t\t%d\t%d\n", name, age, phone_number);
    }

    fclose(file);
  }
}