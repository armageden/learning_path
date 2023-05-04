#include <stdio.h>
int main() {
  int *ptr, i, a[5] = {10, 20, 30, 40, 50};
  ptr = &a[0];
  for (i = 0; i < 5; i++) {
    printf("%d\n", *ptr);
    ptr++;
  }
}