#include <stdio.h>
int main()
{
    printf("Give a year");
    int year;
    scanf("%d",&year);
    if (year%400==0) {
    printf("It's a leap year\n");
    }
    else if (year%4==0&&year%100!=0) {
    printf("It's a leap year\n");
    }
    else {
    printf("It's not a leap year\n");
    }
}