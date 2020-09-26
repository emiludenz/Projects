#include <stdio.h>
#include <string.h>

struct Student{
  char name[50];
  int id;
};


int main(){
  struct Student s;
  strcpy(s.name,"Name of student");
  s.id = 1;
  printf("student name: %s\n",s.name);
  printf("student id: %d\n",s.id);


  return 0;
}