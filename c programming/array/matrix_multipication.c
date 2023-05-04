#include "stdio.h"
int main() {
  int sum = 0, _1st[10][10], _2nd[10][10], result[10][10], r1, r2, c1, c2, i, k,
      j;
  printf("Enter rows and columns for 1st matrix : ");
  scanf("%d %d", &r1, &c1);

  printf("Enter rows and columns for 2nd matrix : ");
  scanf("%d %d", &r2, &c2);

  // filter
  while (c1 != r2) {
    printf("Error !!! multipication not possible! set row and column again...");

    printf("Enter rows and columns for 1st matrix : ");
    scanf("%d %d", &r1, &c1);

    printf("Enter rows and columns for 2nd matrix : ");
    scanf("%d %d", &r2, &c2);
  }

  // taking row and col for 1st matrix
  printf("\nEnter elements for first matrix\n");
  for (i = 0; i < r1; i++) {

    for (j = 0; j < c1; j++) {
      printf("1st [%d][%d] = ", i, j);
      scanf("%d", &_1st[i][j]);
    }
  }

  // taking row and col for 2nd matrix
  printf("\nEnter elements for second matrix\n");
  for (i = 0; i < r2; i++) {

    for (j = 0; j < c2; j++) {
      printf("2nd [%d][%d] = ", i, j);
      scanf("%d", &_2nd[i][j]);
    }
  }
 

  // printing 1st matrix
  printf("First matrix\n");
  for (i = 0; i < r1; i++) {

    for (j = 0; j < c1; j++) {
      printf("%d ", _1st[i][j]);
    }
    printf("\n");
  }

  // printing 2nd matrix
  printf("\n\nSecond matrix\n");
  for (i = 0; i < r2; i++) {

    for (j = 0; j < c2; j++) {
      printf("%d ", _2nd[i][j]);
    }
    printf("\n");
  }
 // multipling matrix

  for (i = 0; i < r1; i++) {
    for (j = 0; j < c2; j++) {
      for (k=0; k<c1; k++) {
      sum = sum + _1st[i][k] * _2nd[k][j];
      }
      result[i][j] = sum;
      sum=0;
    }
    
  }

  //printing result
  printf("\n\nResult matrix");
  for (i = 0; i < r1; i++) {
printf("\n");
    for (j = 0; j < c2; j++) {
      printf("%d ", result[i][j]);
      
    }printf("\n");
  }
}