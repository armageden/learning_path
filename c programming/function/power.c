#include "stdio.h"
void calculate_power(double base, double exp) {
  double i, result = 1;
  for (i = 1; i <= exp; i++) {
    result = result * base;
  }
  printf("%.1lf\n", result);
}
int main() {
  double base, exp;
  printf("Enter a number and exponent : ");
  scanf("%lf %lf", &base, &exp);
  calculate_power(base, exp);
}