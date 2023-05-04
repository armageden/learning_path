#include <stdio.h>
#include <string.h>
int main() {
  char ch, str[100];
  int i, vowel, consonent, digit, word, special;
  i = vowel = consonent = digit = word = special = 0;
  printf("Enter a string : ");
  gets(str);

  while ((ch = str[i]) != '\0') {
    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
        ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {

      vowel++;

    } else if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
      consonent++;
    } else if (ch >= '0' && ch <= '9') {
      digit++;
    } else if (ch == ' ') {
      word++;
    } else {
      special++;
    }
    i++;
  }
  word++;
  printf("Number of Vowels = %d\n", vowel);
  printf("Number of Consonents = %d\n", consonent);
  printf("Number of Words = %d\n", word);
  printf("Number of Digits = %d\n", digit);
  printf("Number of Special Characters = %d\n", special);
}