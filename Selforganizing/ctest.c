#include <stdio.h>
int main(int argc, char const *argv[]){
	// This will print the name of the program
	printf("%s\n", argv[0] );	
	
	// This will print everything in the *argv[]
	if (argc > 1)
		for (int i = 1; i < argc; ++i){
			printf("%s\n", argv[i] );
		}

	return 0;
}