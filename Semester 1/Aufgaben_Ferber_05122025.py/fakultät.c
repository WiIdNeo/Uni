#include <stdio.h>

int fak(int x) {
    if (x == 0) {
        return 1;
    } else {
        printf("%d\n", x);   // print current value
        return x * fak(x - 1);
    }
}

int main() {
    FILE *file;
    int x, y;

    printf("Enter an integer: ");
    scanf("%d", &x);

    y = fak(x);

    printf("Factorial: %d\n", y);

    file = fopen("fak.txt", "w");
    if (file != NULL) {
        fprintf(file, "%d\n", y);
        fclose(file);
    } else {
        printf("Error opening file!\n");
    }

    return 0;
}

