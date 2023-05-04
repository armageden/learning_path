#include "stdio.h"
#include "string.h"
struct person {
  int age;
  char name[50];
  float salary;
};
int main(){
    struct person person[4];
    int i;
    
    //Input Loop
    for (i=0; i<4; i++) {
    printf("Enter Info for person%d\n",i+1);
    printf("Enter Name : ");
    scanf("%s",&person[i].name);

    printf("Enter Age : ");
    scanf("%d",&person[i].age);
    printf("Enter Salary : ");
    scanf("%f",&person[i].salary);
    }
    //Output Loop
    for (i=0; i<4; i++) {
    printf("Info for person%d\n",i+1);
    printf("Name : %s\n",person[i].name);
    printf("Age : %d\n",person[i].age);
    printf("Salary : %f\n",person[i].salary);
    
    }
}