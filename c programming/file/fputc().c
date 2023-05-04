#include <stdio.h>
#include <string.h>
int main(){
    FILE *file;
    char name[20]="Farhan Tanvir";
    int len=strlen(name),i; 
    file=fopen("test.txt", "w");
    if (file==NULL) {
    printf("File not found\n");
    }
    else {
    printf("File opened\n");
    for (i=0;i<len; i++) {
    fputc(name[i],file);
    }
    printf("The file has been written successfully!\n");
    fclose(file);
    }
}