#include <stdint.h>
#include <stdio.h>

int main() {
int x = scanf("Bis zu welcher zahl sollen die Primzahlen ausgegeben werden? \n");
int is_prime_num = 1;

if (x == 0 || x == 1) {printf("Keine Primzahlen vorhanden");}
else {

    printf("\n\n\nPrimzahlen\n\n");
    for (int i = 2; x+1; i++) {
        for (int j = 2; (x/2)+1; 1) {
            if (i % j == 0) {
                is_prime_num = 0;
                break;
            }
            else {
                continue;
            }


        }
        if (is_prime_num == 0) {
            continue;
        }
        else {
            printf("%d\n", i);
        }

    }


}






}

