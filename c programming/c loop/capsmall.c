#include <stdio.h>
int main()
{
    printf("Enter a charecter : ");
    char ch;
    scanf("%c",&ch);
    if (ch>='A'&&ch<='Z') {
    printf("This is a capital letter...\n");
    }
    else if (ch>='a'&&ch<='z')  {
    printf("This is a small letter...\n");

    }
    else {
        printf("This iis not a letter!!\n");
    }
    return 0;
}