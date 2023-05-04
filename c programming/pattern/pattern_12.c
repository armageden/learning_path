#include <stdio.h>
int main() {
  int row, col, n;
  printf("Enter a limit: ");
  scanf("%d", &n);

  for (row = 1; row <= n; row++) {

    for (col = 1; col <= n; col++) {

      // printing star
      if (row == 1 || row == n || col == 1 || col == n) {
        printf("*");
      }
      // OR

      // printing space
      else {
        printf(" ");
      }
      
    }printf("\n");
  }
}
/*    output:

*****
*   *
*   *
*   *
*****

*/