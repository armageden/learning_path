#include <stdio.h>
struct Contact {
  char name[50];
  char phone[50];
  char email[50];
};
void addContact() {
  FILE *file;
  file = fopen("cotact.txt", "a");
  if (!file) {
    printf("File doesn't exit!!");
  } else {
    struct Contact contact;
    fflush(stdin);
    printf("Enter Name: ");
    fgets(contact.name, sizeof(contact.name), stdin);

    printf("Enter phone: ");
    fgets(contact.phone, sizeof(contact.phone), stdin);

    printf("Enter Email: ");
    fgets(contact.email, sizeof(contact.email), stdin);

    fprintf(file, "%s%s%s", contact.name, contact.phone, contact.email);
    fclose(file);
    printf("Added to contact");
  }
}
void displayConatct() {
  struct Contact contact;
  FILE *file;
  file = fopen("cotact.txt", "a");
  if (!file) {
    printf("File doesn't exit!!");
  } else {
    printf("Contacts.\n");

    while (fscanf(file, " %[^\n] %[^\n] %[^\n]", contact.name, contact.phone,
                  contact.email) != EOF) {
      printf("Name: %s\nPhone: %s\nEmail: %s\n", contact.name, contact.phone,
             contact.email);
    }
    fclose(file);
  }
}
int main() {
  addContact();
  displayConatct();
  int choice;
  do {
    printf("\n Contace management system\n");
    printf("1.Add Contact\n");
    printf("2.Display Contact\n");
    printf("3.Exit \n");
    printf("Enter your choice: \n");
    scanf("%d", &choice);

    switch (choice) {
    case 1:
      addContact();
      break;
    case 2:
      displayConatct();
      break;
    case 3:
      printf("Exiting....!\n");
      break;
    default:
      printf("Choose again!...!\n");
    }
  } while (choice != 3);
}