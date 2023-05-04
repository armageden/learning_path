#include <stdio.h>
union test {
  int x, y;
};

int main() {
  union test t1;
  t1.x = 109;
  printf("x=%d\n", t1.x);//x=190
  printf("y=%d\n", t1.y);//y=190

  t1.y = 40;
  printf("x=%d\n", t1.x);//x=40
  printf("y=%d\n", t1.y);//y=40
}