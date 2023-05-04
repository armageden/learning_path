#include <stdio.h>
struct book{
    char name[30];
    double price;
};
int main(){
typedef struct book Book ;
Book b={"My life's joke",769.65};
printf("Book name: %s,price = %.3lf\n",b.name,b.price);

}