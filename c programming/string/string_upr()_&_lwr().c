#include <stdio.h>
#include <string.h>
//creating strlwr() 
char *strlwr(char *s) {
  char *t = s;

  if (!s) {
    return 0;
  }

  int i = 0;
  while (*t != '\0') {
    if (*t >= 'A' && *t <= 'Z') {
      *t = *t + ('a' - 'A');
    }
    t++;
  }

  return s;
}

//creating strupr()
char *strupr(char *u) {
  char *v = u;

  if (!u) {
    return 0;
  }

  int i = 0;
  while (*v != '\0') {
    if (*v >= 'a' && *v <= 'z') {
      *v = *v + ('A' - 'a');
    }
    v++;
  }

  return u;
}
int main() {
  char str1[] = "FARHAN", str2[] = "tanvir";

  printf("Lower = %s\n", strlwr(str1));
  printf("Upper = %s\n", strupr(str2));
}