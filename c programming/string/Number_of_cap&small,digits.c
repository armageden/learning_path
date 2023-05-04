#include <stdio.h>
int main() {
  char ch, str[100];
  int i, capital, small, digit;
  i = small = capital = digit = 0;
  printf("Enter a string : ");
  gets(str);

  while ((ch = str[i]) != '\0') {

    if (ch >= 'A' && ch <= 'Z') {
      capital++;
    } else if (ch >= 'a' && ch <= 'z') {
      small++;
    } else if (ch >= '0' && ch <= '9') {
      digit++;
    }
    i++;
  }
  printf("Number of capital = %d, small = %d , digit = %d\n", capital, small,
         digit);
}