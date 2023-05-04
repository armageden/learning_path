#include "stdio.h"
int main(){
    int i,j,a[3][4];
//this collects the array
for (i=0; i<3; i++) {
for (j=0;j<4; j++) {
    printf("a[%d][%d] = ",i,j);
scanf("%d",&a[i][j]);
}
printf("\n");
}

//this prints the array
printf("a =");
for (i=0; i<3; i++) {
  printf("\t"); 
   for (j=0;j<4; j++) {
    printf("%d ",a[i][j]);
    }printf("\n");
    }
}