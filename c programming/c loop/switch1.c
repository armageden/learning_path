#include <stdio.h>
int main() {
  int digit;
  printf("Enter a digit & it will be spelled : ");
  scanf("%d",&digit);

  switch (digit) {

  case 0:
    printf("Zero\n");
    break;
  case 1:
    printf("One\n");
    break;
  case 2:
    printf("Two\n");
    break;

  default:
    printf("Invalid digit!!");
    /* it is not fully done as I am lazy as heck
    but it is good enough for a beta...*/
  }
}