#include <stdio.h>

int size(int n){
	float fn = n;
	n = (fn-1)*((fn-1)/2)+((fn-1)/2);
	return n;
} 

struct pair{
	int fst;
	int snd;
};

int main(){
	int n = 4;
	int array[4] = {1,2,3,4};
	int len = size(n);
	struct pair pairs[len];
	int count = 0;
	
	for(int i = 0; i < sizeof(array)/sizeof(array[0]); i++){
		for(int j = i+1; j < sizeof(array)/sizeof(array[0]); j++){
			struct pair p;
			p.fst = array[i];
			p.snd = array[j];
			pairs[count] = p;
			count++;
		}
	}
	for (int i = 0; i < len; ++i){
		printf("fst:%d\tsnc:%d\n",pairs[i].fst,pairs[i].snd );
	}
	
	
	
	return 0;
}