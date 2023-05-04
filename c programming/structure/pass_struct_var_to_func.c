#include "stdio.h"
#include <string.h>
struct person {
  char name[50];
  int age;
  float salary;
};
void display(struct person p) {
  printf("Name : %s\n", p.name);
  printf("Age : %d\n", p.age);
  printf("Salary : %f\n", p.salary);
}
int main() {
  struct person person1;
  strcpy(person1.name, "Farhan Tanvir");
  person1.age = 27;
  person1.salary = 123456.7890;
  display(person1);
}