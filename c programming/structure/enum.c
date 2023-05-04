#include <stdio.h>
enum days_of_week{sun=1,mon,tue,wed,thu,fri,sat};
int main(){
    enum days_of_week day1,day2;
    day1=sun;
    printf("Day 1 =%d\n",day1);
}