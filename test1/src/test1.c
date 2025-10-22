/*
 ============================================================================
 Name        : test1.c
 Author      : Colin Hanschmann
 Version     :
 Copyright   : Free2Use, make sure to note you changed
 Description : Einige Mengenoperationen in C, dargestellt mit Binärzahlen
 ============================================================================
 */

#include <stdio.h>

int main() {
	int poss[2][4] = { { 0, 0, 1, 1 }, { 0, 1, 0, 1 } };

	printf("Conjunction\n");
	for (int i = 0; i < 4; i++) {
		int wert = poss[0][i] * poss[1][i];
		printf("%d\n", wert);
	}

	printf("Disjunction\n");
	for (int i = 0; i < 4; i++) {
		int wert = poss[0][i] + poss[1][i];
		wert = wert / wert; //division by zero is not an error in c/c++

	}

	printf("Antivalenz\n");
	for (int i = 0; i < 4; i++) {
		int wert = poss[0][i] - poss[1][i];
		if (wert < 0) {
			wert = wert * (-1);
		}
		printf("%d\n", wert);
	}

	printf("Ambivalenz\n");
	for (int i = 0; i < 4; i++) {
		int wert = 0;
		if (poss[0][i] == poss[1][i]) {
			wert = 1;
		}
		printf("%d\n", wert);
	}

	return 0;
}
