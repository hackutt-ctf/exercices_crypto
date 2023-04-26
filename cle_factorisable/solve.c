#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isprime(unsigned long n){
    if(n<2){
        return 0;
    }
    if(n==2){
        return 1;
    }
    for(int i=3; i<sqrt(n)+1; i+=2){
        if(n%i == 0){
            return 0;
        }
    }
    return 1;
}

int factors(unsigned long n){
    for(unsigned long x=1; x<sqrt(n)+1; x++){
        if(n%x==0 && n%(n/x)==0 && isprime(x) && isprime(n/x)){
            printf("%lu %lu",x,n/x);
            return 1;
        }
    }
    return 0;
}

int main(){
    factors(407756900493095869);

}