#include<stdio.h>
int main()
{ double fah,cel ;
int c;
    printf("temperature conversion option\n1.Fahrenhight to Celcious\n2. Celcious to Fahrenhight\n Enter your choice : ");
    scanf("%d",&c);
    switch (c) {
    case 1:printf("enter the value to convert :");
    scanf("%lf",&fah);
    cel=(fah-32)/1.8;
    printf("the result is %.3lf C\n",cel);
    break;
    case 2:printf("enter the value to convert :");
    scanf("%lf",&cel);
    fah=(1.8*cel)+32;
    printf("the result is %.3lf F\n",fah);
    break;
    }
}