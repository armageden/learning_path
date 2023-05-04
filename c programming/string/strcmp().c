#include <stdio.h>
#include <string.h>
int main(){
    char str1[]="Tanvir",str2[]="Tanvir";
    int d=strcmp(str1,str2);
if (d==0) {
printf("Strings are equal\n");
}
else {
printf("Strings are not equal\n");
}
}