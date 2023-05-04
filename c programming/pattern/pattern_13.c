#include <stdio.h>
int main()
{

    int n,row,col;
    printf("Enter a limit :");
    scanf("%d",&n);

    for (row=1; row<=n; row++) {
    
        for (col=1; col<=n; col++) {
        
        //printing a star..
            if (row==col||row==n||col==1) {
                printf("*");
            }
            else {
            printf(" ");
            }
        }
printf("\n");

    }

}
/*         
           output: 

*     
**    
* *   
*  *  
*   * 
******

           */