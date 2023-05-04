#include <stdio.h>
union test {
    int x,y;
};
union test2{
    char ch;
    int x;
};
union test3{
    char name[20];
    double d;
};
int main(){
    union test t1;
    union test2 t2;
    union test3 t3;
printf("sizeof(test1) = %ld\n",sizeof(t1));
printf("sizeof(test1) = %ld\n",sizeof(t2));
printf("sizeof(test1) = %ld\n",sizeof(t3));
}