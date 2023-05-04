#include <stdio.h>
int main(){
    int x=10,*p;
    p=&x;

printf("Value of x = %d\n",x);
printf("Address of x = %d\n",&x);
printf("Value of x = %d\n",*p);
printf("Address of x = %d\n",p);
}