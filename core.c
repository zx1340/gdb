#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void a(){
    printf("Called function a\n");
}

void b(){
    printf("Called function b\n");
}

void c(){
    printf("Called function c\n");
}

void d(){
    printf("Called function d\n");
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("GIVE SOME NUMBER\n");
        return 0;
    }
    int theNumber = atoi(argv[1]);
    printf("You entered [%d]\n", theNumber);            // entering 10 or 1 outputs [49], entering 9 outputs [57]
    switch (theNumber){
        case 1:
            a();
            break;
        case 2:
            b();
            break;
        case 3:
            c();
            break;
        default:
            d();
    }   
    return 1;
}
