#include "stdio.h"
int main() {
  int numTerm, first=2, second=1;
  printf("Enter the number of terms for the lucas series : ");
  scanf("%d", &numTerm);
  printf("%d %d",first,second);
  for (int i = 0; i <= numTerm; i++) {
    int next = first + second;
    printf(" %d", next);
    first=second;
    second=next;
  }
  printf("\n");
}