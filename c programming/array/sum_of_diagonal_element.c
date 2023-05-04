#include <stdio.h>
int main() {
  int i, j, matrix[10][10], row, col, sum = 0;

  // getting row and columns..

  printf("Enter rows and columns for the matrix : ");
  scanf("%d %d", &row, &col);

//filter

while (col != row) {
    printf("Error !!! multipication not possible! set row and column again...");

    printf("Enter rows and columns for 1st matrix : ");
    scanf("%d %d", &row, &col);
    }
  // getting the element of the matrix

  printf("\nEnter elements for the matrix\n");
  for (i = 0; i < row; i++) {
    for (j = 0; j < col; j++) {
      printf("Matrix [%d][%d] = ", i, j);
      scanf("%d", &matrix[i][j]);
    }
  }

  // printing the matrix
  printf("Matrix\n");
  for (i = 0; i < row; i++) {

    for (j = 0; j < col; j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }

  // sum of diagonal elements
  for (i = 0; i < row; i++) {
    for (j = 0; j < col; j++) {
      if (i == j) {
        sum = sum + matrix[i][j];
      }
    }
  };
  printf("Sum of diagonal element of Matrix is %d\n", sum);
}
