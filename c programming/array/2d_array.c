#include "stdio.h"
int main(){
    int i,j,a[3][4]={{5,6,7,7},{6,4,4,7,},{7,89,67,75}};
    for (i=0; i<3; i++) {
    for (j=0;j<4; j++) {
    printf("%d ",a[i][j]);
    }printf("\n");
    }
}