#include "stdio.h"
void diplay(int a[]){
    int  i;
    for (i=0;i<7; i++) {
    printf("%d ",a[i]);
    }
}
int main(){
    int num[]={10,12,13,14,16,7,9};
    diplay(num);
}