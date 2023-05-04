#include <stdio.h>
int main(){
    char s1[30];
    printf("Enter your full name : ");
  
  /*  scanf("%s",&s1);*/ //this doesn't work for spaces as it drops the elements after space..
  //so we have to use gets() function.

  gets(s1);
    printf("Full name is %s\n",s1);
}