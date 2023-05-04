#include "stdio.h"
int main() {
  int row, col, i, j, a[10][10], b[10][10], c[10][10];

  printf("enter the number of rows and coloums : ");
  scanf("%d %d", &row, &col);

  // fetching a matrix
  for (i = 0; i < row; i++) {
    for (j = 0; j < col; j++) {
      printf("a[%d][%d] = ", i, j);
      scanf("%d", &a[i][j]);
    }
    printf("\n");
  }

  // fetching b matrix
  for (i = 0; i < row; i++) {
    for (j = 0; j < col; j++) {
      printf("b[%d][%d] = ", i, j);
      scanf("%d", &b[i][j]);
    }
    printf("\n");
  }
  /// printing a matrix
  printf("a =");
  for (i = 0; i < row; i++) {
    printf("\t");
    for (j = 0; j < col; j++) {
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }

  // printing b matrix
  printf("\nb =");
  for (i = 0; i < row; i++) {
    printf("\t");
    for (j = 0; j < col; j++) {
      printf("%d ", b[i][j]);
    }
    printf("\n");
  }

  // addition of matrix
  for (i = 0; i < row; i++) {
    for (j = 0; j < col; j++) {
      c[i][j] = a[i][j] + b[i][j];
    }
  }

  // printing c matrix

  printf("\nc =");
  for (i = 0; i < row; i++) {
    printf("\t");
    for (j = 0; j < col; j++) {
      printf("%d ", c[i][j]);
    }
    printf("\n");
  }
}