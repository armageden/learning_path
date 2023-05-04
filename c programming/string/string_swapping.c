#include <stdio.h>
#include <string.h>
int main() {
  char str1[] = "Farhan", str2[] = "Tanvir", temp[50];

  // swapping

  strcpy(temp, str1);
  strcpy(str1, str2);
  strcpy(str2, temp);

  // swapped strings

  printf("string1 = %s\n", str1);
  printf("string2 = %s\n", str2);
}