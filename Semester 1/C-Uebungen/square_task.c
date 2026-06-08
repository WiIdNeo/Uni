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
	int ex1 = 0;
	int zx2 = 0;
	int dx3 = 0;
	int vx4 = 0;
	int counter;
	int picture[6][6] = {
			{0,0,1,1,0,0},
			{0,1,1,1,1,0},
			{1,1,1,1,1,1},
			{1,1,1,1,1,1},
			{0,1,1,1,1,0},
			{0,0,1,1,0,0}
	};
	int rows = sizeof(picture) / sizeof(picture[0]);
	int cols = sizeof(picture[0]) / sizeof(picture[0][0]);
	printf("Rows: %d, Cols %d\n", rows, cols);

	for (int i = 0; i < rows; i++) {
	    for (int j = 0; j < cols; j++) {
	        if (picture[i][j] == 1) {
	            ex1++;

	            // 2x2
	            if (i < rows-1 && j < cols-1) {
	                if (picture[i+1][j] == 1 && picture[i][j+1] == 1 && picture[i+1][j+1] == 1) {
	                    zx2++;

	                    // 3x3
	                    if (i < rows-2 && j < cols-2) {
	                        if (picture[i][j+2] == 1 && picture[i+1][j+2] == 1 && picture[i+2][j+2] == 1 &&
	                            picture[i+2][j+1] == 1 && picture[i+2][j] == 1) {
	                            dx3++;

	                            // 4x4
	                            if (i < rows-3 && j < cols-3) {
	                                if (picture[i][j+3] == 1 && picture[i+1][j+3] == 1 &&
	                                    picture[i+2][j+3] == 1 && picture[i+3][j+3] == 1 &&
	                                    picture[i+3][j+2] == 1 && picture[i+3][j+1] == 1 &&
	                                    picture[i+3][j] == 1) {
	                                    vx4++;
	                                }
	                            }
	                        }
	                    }
	                }
	            }
	        }
	    }
	}

	counter = ex1 + zx2 + dx3 + vx4;
	printf("Ein-mal-Eins-Vierecke: %d\nZwei-mal-zwei-Viereck: %d\nDrei-mal-Drei-Vierecke: %d\nVier-mal-Vier-Vierecke: %d\nGesamt: %d\n", ex1, zx2, dx3, vx4, counter);


	return 0;
}