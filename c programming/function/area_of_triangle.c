#include <stdio.h>
void area_of_triangle(double base,double height){
    double area=0.5*base*height;
    printf("The area of the triangle is %.1lf\n",area);
}
int main(){
    printf("Enter base and height of the triangle : ");
    double b,h;
    scanf("%lf %lf",&b,&h);
    area_of_triangle( b, h);

}