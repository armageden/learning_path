#include "stdio.h"

//global structure
struct person{
    int age;
    float salary;
};
int main(){
  struct person person1,person2;
    //For person1
    printf("For person1\n");
    printf("Enter age : ");
    scanf("%d",&person1.age);
    printf("Enter salary : ");
    scanf("%f",&person1.salary);

    printf("Person1 : \n");
    printf("Age = %d\n",person1.age);
    printf("Salary = %.2f\n",person1.salary);

    //For person2
    printf("For person1\n");
    printf("Enter age : ");
    scanf("%d",&person2.age);
    printf("Enter salary : ");
    scanf("%f",&person2.salary);
    
    printf("Person1 : \n");
    printf("Age = %d\n",person2.age);
    printf("Salary = %.2f\n",person2.salary);
}