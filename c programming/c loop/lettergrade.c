#include <stdio.h>
int main()
{
    printf("Enter your marks : ");
    float mark;
    scanf("%f",&mark);

    if (mark>100 ||mark<0) {
    printf("invalid input\n");
    }
    else if (mark>=80&&mark<=100) {
    printf("You got A+\n");
    }
    else if (mark>=70&&mark<=79) {
    printf("You got A\n");
    }
    else if (mark>=60&&mark<=69) {
    printf("You got A-\n");
    }
    else if (mark>=50&&mark<=59) {
    printf("You got B\n");
    }
    else if (mark>=40&&mark<=49) {
    printf("You got C\n");
    }
    else if (mark>=35&&mark<=39) {
    printf("You got D\n");
    }
    else if (mark>=33&&mark<=34) {
    printf("You got E\n");
    }
    else {
    printf("You have failed!!!!!\n");
    }

}