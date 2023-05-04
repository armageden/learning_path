#include<stdio.h>
int main()
{
    int a=32,b=12,c;

    c=a&b;
    printf("a&b=%d\n",c);
    c=a|b;
    printf("a|b=%d\n",c);
    c=a^b;
    printf("a^b=%d\n",c);
}