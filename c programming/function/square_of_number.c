#include <stdio.h>
void sqr(int a){
    printf("The square of the number is %d\n",a*a);
}
int main(){
    int num;
    printf("Enter a number : ");
    scanf("%d",&num);
    sqr(num);
}