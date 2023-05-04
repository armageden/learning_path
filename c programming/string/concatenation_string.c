#include <stdio.h>
int main(){
    char str1[50]="My name is ",str2[]="Farhan Tanvir";

    int j=0,i=0,len=0;
    while (str1[i]!='\0') {
    i++,len++;
    }
    while (str2[j]!='\0') {
    str1[len+j]=str2[j];
    j++;
    }
    printf("concatenation of the strings = %s\n",str1);
}