#include "stdio.h"
// funtion to get the first day of the year..
int get_first_day(int year) {
  int day = (year * 365 + ((year - 1) / 100) + ((year - 1) / 400)) % 7;
  return day;
}

int main() {
  char *month[] = {"January",   "February", "March",    "April",
                   "May",       "June",     "July",     "August",
                   "September", "October",  "November", "December"};
  int i, days_in_month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
         total_days, j, week_days = 0, year, space_count = 0;

  // to collect the year..
  printf("Enter the year you want to view : ");
  scanf("%d", &year);
  printf("\n\n%d\n\n", year);

  // to check if it is a  leap year...
  if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
    days_in_month[1] = 29;
  }
  // get the firt day of thr year...
  week_days = get_first_day(year);

  // for printing the generic format...
  for (i = 0; i < 12; i++) {
    printf("\n--------------------------%s-------------------------\n",
           month[i]);
    printf("\n  Sun   Mon   Tue   Wed   Thu   Fri   Sat\n\n");
    for (space_count = 1; space_count <= week_days; space_count++) {
      printf("      ");
    }
    total_days = days_in_month[i];
    for (j = 1; j <= total_days; j++) {
      printf("%5d", j);
      week_days++;
      if (week_days > 6) {
        week_days = 0;
        printf("\n");
      }
    }
  }
  printf("\n");
  return 0;
}