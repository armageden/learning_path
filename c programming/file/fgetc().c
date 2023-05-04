#include <stdio.h>
int main(){
    FILE *file;
    char ch;
    file=fopen("text.txt","r");
    if (file==NULL) {
    printf("File doesn't exist!\n");
    }
    else {
    printf("file is opened\n");
    while (!feof(file)) { //!feof is "not untill the end of file"...
    ch=fgetc(file);
    printf("%c",ch);
    }
    fclose(file);
    }
}