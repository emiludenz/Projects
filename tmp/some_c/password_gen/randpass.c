#include <stdlib.h>
#include <time.h>
#include <stdio.h>

int get_random_int(int start, int end){
	int r = rand()%128;
	if(r < start){
		r = (start-r)+r;
	}
	return r;
}


int check_args(int argc, char* argv[]){	
	if(argc != 2){
		printf("Must provide a desired length of password\n");
		exit(-1);
	}
	int length = atoi(argv[1]);
	if(length < 8){
		printf("Password must be 8 characters or longer\n");
		exit(-1);
	}
	return length;
}


const char* create_password(int length){
	char password[length];
	int start = 33;
	int end = 128;
	int len = end-start;
	
	for(int i = 0; i < length; i++){
		int random_int = get_random_int(start, end);
		char f = random_int;
		password[i] = f;
	}
	password[length-1] = 0;	
	char * pass = password;
	return pass;
}

int main(int argc, char* argv[]){
	srand(time(NULL));
	int length = check_args(argc,argv);
	printf("%s\n",create_password(length));
	return 0;
}
