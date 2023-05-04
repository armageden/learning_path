// leaner search...
#include "stdio.h"
int main() {
  int value, i,
      pos = -1,
      num[] = {2347274, 2,  45, 2345, 5,  45,  45, 4,         2,    423, 423,
               25,      2,  54, 556,  5,  44,  2,  563452445, 7646, 3,   535,
               66,      4,  4,  4,    65, 6,   56, 6,         45,   345, 344643,
               534,     45, 64, 643,  53, 645, 6,  53,        356,  456, 45};

  printf("Enter a value you want to search : ");
  scanf("%d", &value);
  for (i = 0; i < 44; i++) {
    if (value == num[i]) {
      pos = i + 1;
      break;
    }
  }
  if (pos == -1) {
    printf("The number is not found\n");
  } else {
    printf("The position of the %d is %d\n", value, pos);
  }
}