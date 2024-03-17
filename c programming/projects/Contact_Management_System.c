#include <stdio.h>
void addContact() {
  FILE *file;
  file = fopen("cotact.txt", "a");
  if (!file) {
    printf("File doesn't exit!!");
  } else {

    char name[50];
    char phone[50];
    char email[50];
    printf("Enter Name: ");
    fgets(name, sizeof(name), stdin);
    printf("Enter phone: ");
    fgets(phone, sizeof(phone), stdin);
    printf("Enter Email: ");
    fgets(email, sizeof(email), stdin);

    fprintf(file,"%s%s%s",name,phone,email);
    fclose(file);
    printf("Added to contact");
  }
}
int main(){
    addContact();
}