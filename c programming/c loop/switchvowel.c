#include <stdio.h>
int main() {
  char ch;
  printf("Enter a Letter : ");
  scanf("%c",&ch);
  switch (ch) {
  case 'a':
    printf("It's a vowel\n");
    break;
  case 'e':
    printf("It's a vowel\n");
    break;
  case 'i':
    printf("It's a vowel\n");
    break;
  case 'o':
    printf("It's a vowel\n");
    break;
  case 'u':
    printf("It's a vowel\n");
    break;
  case 'A':
  case 'E':
  case 'I':
  case 'O':
  case 'U':
    printf("It's a vowel\n");
    break;
  default:
    printf("It's a consonent\n");
    break;
  }
  return 0;
}