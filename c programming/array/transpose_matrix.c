#include "stdio.h"
int main() {
  int matrix[10][10], transpose[10][10], i, j, row, col;

  printf("Enter the number of rows and columns for the martix : ");
  scanf("%d %d", &row, &col);

  // getting elements for the matrix

  for (i = 0; i < row; i++) {
    for (j = 0; j < col; j++) {
      printf("Matrix [%d][%d]=", i, j);
      scanf("%d", &matrix[i][j]);
    }
  }
  // printing the matrix
  printf("\nMatrix\n");
  for (i = 0; i < row; i++) {
    for (j = 0; j < col; j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }
  //transposing the matrix
    for (i=0; i<row; i++) {
    for (j=0; j<col;j++) {
    transpose[j][i]=matrix[i][j];
    }
    }
printf("\nTranspose Matrix\n");
  for (i = 0; i < col; i++) {
    for (j = 0; j <row ; j++) {
      printf("%d ", transpose[i][j]);
    }
    printf("\n");
  }
}