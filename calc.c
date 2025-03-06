#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    
    double n=0.00;
    double nn=0.00;
    int t=1;
    char nm[1024]="\0"; 
    
    printf("\033c\033[43;30m\n0.00\n",n);
    while(t){
        
        fgets(nm,79,stdin);
        if(nm[0]!='\n'){
            nn=atof(nm);
            n=n+nn;
        }else{
            t=0;
        }
            printf("\033[43;30m%f\n",n);
    }
    return 0;
}
