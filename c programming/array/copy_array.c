#include "stdio.h"
int main() {
  int a1[5] = {10, 20, 30, 40, 50}, a2[5], i;
  printf("Array 1 : ");
  for (i = 0; i < 5; i++) {
    printf("%d ", a1[i]);
  }
  for (i=0; i<5; i++) { //this copies all the elements from the a1 array to a2 array
  a2[i]=a1[i];
  }
  printf("\nArray 2 : ");
  for (i = 0; i < 5; i++) {
    printf("%d ", a2[i]);
  }
  printf("\n");
}