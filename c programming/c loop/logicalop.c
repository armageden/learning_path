#include <stdio.h>
int main()
{
    char ch;
    printf("Enter a letter : ");
    scanf("%c",&ch);
    if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') {
    printf("This is a vowel\n");
    }
    else {
    printf("This is a consonent\n");
    }
}