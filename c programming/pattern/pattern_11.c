#include <stdio.h>
int main()
{   int row,n,col;
    printf("Enter a limit :");
    scanf("%d",&n);
//upper part..
    for (row=1;row<=n;row++) {
    
    //for printing space 
    for (col=1;col<=n-row ;col++ ) {
    printf(" ");
    }

    //for printing *
    for (col=1; col<=row; col++) {
    printf("* ");
    }
    printf("\n");
    }


//lower part...
    for (row=n-1;row>=1;row--) {
    
    //for printing space 
    for (col=1;col<=n-row ;col++ ) {
    printf(" ");
    }

    //for printing *
    for (col=1; col<=row; col++) {
    printf("* ");
    }
    printf("\n");
    }
}