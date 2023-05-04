#include <stdio.h>
int main() {
  int i, j, matrix[10][10], row, col, upper_sum = 0, lower_sum = 0;

  // getting row and columns..

  printf("Enter rows and columns for the matrix : ");
  scanf("%d %d", &row, &col);

  // filter

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

    //sum of upper & lower triangle elements
    for (i=0; i<row; i++) {
    for (j=0; j<col;j++) {
    if (i<j) {
    upper_sum=upper_sum+matrix[i][j];
    }
    if (i>j) {
    lower_sum=lower_sum+matrix[i][j];
    }
    }
    }
printf("\nSum of upper triangle elements = %d\n",upper_sum);
printf("\nSum of lower triangle elements = %d\n",lower_sum);
}