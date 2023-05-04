#include <stdio.h>
int main()
{
    int row,n,col;
    printf("Enter a limit : ");
    scanf("%d",&n);
    for (row=1; row <=n; row++) {
    for (col=1; col<=row; col++) {
    printf("%d ",col);

    }
    printf("\n");
    }

for (row=n-1; row>=1; row--) {
    for (col=1; col<=row; col++) {
    printf("%d ",col);

    }
    printf("\n");
    }

}