

#include <stdio.h>
int main()
{
    int num[100],i,n,max;
    printf("How many number?\n: ");
    scanf("%d",&n);

    for (i=0; i<n; i++) {
    scanf("%d",&num[i]);

    }
    max=num[0];
   for (i=1; i<n; i++) {
   
   
   if (max<num[i]) {
   max=num[i];
  //HERE the value of max changers depending on the numbers... 
   }
   }
   printf("The maximum number is %d\n",max);

}