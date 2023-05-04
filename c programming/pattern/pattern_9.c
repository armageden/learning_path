#include <stdio.h>
int main()
{
    int row,col,n;
    printf("Enter a limit : ");
    scanf("%d",&n);
    for (row=1; row<=n; row++) {


      //printing space....  
    for (col=1; col<=n-row; col++) {
        printf(" ");}

 /* //if u want to print  numbers
    for (col=1; col<=2*row-1; col++){ 
    printf("%d",col Or row);   */
        //printing *
    for (col=1; col<=2*row-1; col++){ 
    printf("*");
    }
    printf("\n");
   } 


//the bottom part
 
    for (row=n; row>=1; row--) {


      //printing space....  
    for (col=1; col<=n-row; col++) {
        printf(" ");}

 /* //if u want to print  numbers
    for (col=1; col<=2*row-1; col++){ 
    printf("%d",col Or row);   */
        //printing *
    for (col=1; col<=2*row-1; col++){ 
    printf("*");
    }
    printf("\n");
   } 

}