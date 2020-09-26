#include <stdio.h>
typedef long long unsigned ull;

ull factorial(ull n){
  ull fact = 1;
  for(ull i = 1; i < n+1ull; i++){
    fact *= i;
  }
  return fact;
  
}

ull choose(ull n, ull k) {

    return factorial(n)/(factorial(k)*factorial(n-k));

}

void main(){
	ull out;
    out = choose(  5,  4 );
    printf("%lld\n", out);
    //out = choose( 10,  5 );
    //printf("%lld\n", out);
    //out = choose( 10, 20 );
    //printf("%lld\n", out);
	//out = choose(  1,  1 );
	//printf("%lld\n", out);
    out = choose( 52,  5 );
    printf("%lld\n", out);
}