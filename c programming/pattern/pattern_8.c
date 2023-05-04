#include <stdio.h>
int main()
{
    int row,col,n;
    printf("Enter a limit : ");
    scanf("%d",&n);

    for (row=n; row>=1; row--) {


      //printing space....  
    for (col=1; col<=n-row; col++) {
        printf(" ");}


        //printing *
    for (col=1; col<=2*row-1; col++){ 
    printf("*");
    }
    printf("\n");
   } 
}