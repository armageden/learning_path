#include <stdio.h>
int main()
{
    int x;
    printf("Enter a number : ");
    scanf("%d",&x);

    if (x%2==0) {
    printf("even\n");
    }
    if (x%2!=0) {
    printf("odd\n");
    }


}