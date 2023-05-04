#include <stdio.h>
int main(){
    int x=10,y=20,*p1,*p2,sum;
    p1=&x,p2=&y,sum=*p1+*p2;
    printf("Sum = %d\n",sum);
}