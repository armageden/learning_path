#include "stdio.h"
//global Structure
struct person{
    int age;
    float salary;
};
int main(){
struct person person1,person2;
person1.age=27;
person1.salary=27000.85;

printf("Age of person 1 = %d",person1.age);
printf("Salary of person 1 = %f",person1.salary);


}