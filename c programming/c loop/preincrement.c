#include <stdio.h>
int main()
{ //there is pre-increment so the value of x went from 10 to 11
    int x=10,y=++x;// and y is 11 and x=11
    printf("x=%d y=%d\n",x,y);
    return 0;
}