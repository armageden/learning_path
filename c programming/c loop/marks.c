#include <stdio.h>
int main()
{
    double marks;
    printf("Give your attended number : ");
    scanf("%lf",&marks);
    
    if (marks>100) {
    printf("That's a invalid number\n");
    }
    
    
    else if (marks>=80) {
    printf("you got an A+\n");
    }
    else {
    printf("You didn't get an A+\n");
    }
    if (marks<33) {
    printf("You have failed!!\n");
    }
    
    
    
    
    
    return 0;
}