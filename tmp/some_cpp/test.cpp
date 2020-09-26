#include <iostream>
#include <string.h>

using namespace std;

int get_a_number(){
  return 10;
}







class Person{
  public:
  int age;
  string name;
  
  int get_age(){
    int age;
    cout << "And how old are you?\n";
    cin >> age;
    return age;
  }
  
  string get_name(){
    string name;
    cout << "Hello, what is your name?\n";
    cin >> name;
    return name;
  }
};

int main(){
  Person p;
  p.name = p.get_name();
  p.age = p.get_age();
  cout << "Well hello " << p.name << " are you really " << p.age <<" years old?\n";
  
  char ans;
  cin >> ans;
  if(ans == 'y'){
    cout << "Well okay...\n";
  }
  return 0;
}