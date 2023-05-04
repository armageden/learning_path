#include <stdio.h>
int main(){
    FILE *file;
    char name[30];
    file=fopen("text.txt", "r");
    if (file==NULL) {
    printf("file doesn't exist!!\n");
    }
    else {
    printf("file is opened!\n");
    fscanf(file,"%s",&name);
    printf("%s\n",name);
    fclose(file);
    }

}