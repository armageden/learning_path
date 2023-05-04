#include <stdio.h>
int main(){
    
    typedef char letter;// does the same thig as this char ch;
    // it's more like a alias...
    letter ch='A';
    printf("ch = %c\n",ch);
}