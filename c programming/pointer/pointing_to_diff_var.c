#include <stdio.h>
int main() {
  int *ptr, x = 10, y = 20, z = 30;
  ptr = &x;
  printf("Value of x=%d\n", *ptr);
  ptr = &y;
  printf("Value of y=%d\n", *ptr);
  ptr = &z;
  printf("Value of z=%d\n", *ptr);
}