#include <stdio.h>
#include <string.h>

int main() {
  char str1[50] = "Farhan Tanvir", str2[50];
  int i, len = strlen(str1);

  for (i = 0; i < len; i++) {
    str2[i] = str1[len - 1 - i];
  }
  str2[i] = '\0';
  printf("%s\n", str2);
  int d=strcmp(str1, str2);
  if (d==0) {
  printf("The string is palindrome\n");
  }
  else {
  printf("The string is not palindrome\n");
  }
}