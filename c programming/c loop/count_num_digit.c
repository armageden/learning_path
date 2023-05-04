#include <stdio.h>
int main()
{
   while (1)   //this will make the programme go on ...
 {  int num,count=0;
   printf("Enter a Integar : ");
    scanf("%d",&num);

   

    while (num!=0) {
    num=num/10;
    ++count;
    
    }
    printf("The number of digits are %d\n",count);

}

}