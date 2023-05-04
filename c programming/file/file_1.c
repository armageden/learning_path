#include <stdio.h>
int main(){
    FILE *file;
    file=fopen("test.txt", "w");
    if (file==NULL) {
    printf("File not found\n");
    }
    else {
    printf("File opened\n");
    fclose(file);
    }
}