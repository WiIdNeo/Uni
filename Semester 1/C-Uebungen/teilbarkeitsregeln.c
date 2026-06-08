#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int teilbar_durch_2(char x[50]) {
    int len = strlen(x);
    int digit = x[len - 1] - '0';
    return digit % 2 == 0;

}
int teilbar_durch_3(char x[50], int letters) {
    int y = 0;
    char* endptr;
    do{
      for (int i = 0; i < letters; i++) {
        y = y+(int)x[i];
    }  
    } while (y > 9);
    if (y==3 || y==6 || y==9) {
        return 1;
    }
    else{
        return 0;
    }
    
}
int teilbar_durch_4(char x[50]) {
    int len = strlen(x);
    char num[3];  // 2 characters + null terminator
    num[0] = x[len - 2];
    num[1] = x[len - 1];
    num[2] = '\0';  // Null terminator
    if (atoi(num) == 0) {
        return 1;
    }
    else {
        return 0;
    }
}
int teilbar_durch_5(char x[50]) {
    int len = strlen(x);
    int num;
    num = x[len - 1];
    if ((strlen(x)-1) == 0 || (int)x[-1] == 5) {
        return 1;
    }
    else {
        return 0;
    }
}
int teilbar_durch_6(char x[50], int letters) {
    if (teilbar_durch_2(x) == 1 && teilbar_durch_3(x, letters) == 1) {
        return 1;
    }
    else{
        return 0;
    }
}
int teilbar_durch_7(char x[50]) {
    int rest = atoi(x);
    int z = 0;
    do
    {
        z = rest%10;
        rest = (int)(rest/10) - (z*2);
    } while (rest > 9);
    if (rest == 0 || rest == 7) {
        return 1;
    }
    else{
        return 0;
    }
    

}
int teilbar_durch_8(char x[50]) {
    int len = strlen(x);
    char num[4];  // 2 characters + null terminator
    num[0] = x[len - 3];
    num[1] = x[len - 2];
    num[2] = x[len - 1];
    num[3] = '\0';  // Null terminator
    if ((atoi(num)%8) == 0) {
        return 1;
    }
    else {
        return 0;
    }
}
int teilbar_durch_9(char x[50], int letters) {
    int y = 0;
    char* endptr;
    do{
      for (int i = 0; i < letters; i++) {
        y = y+strlen(x);
    }  
    } while (y > 9);
    if (y==9) {
        return 1;
    }
    else{
        return 0;
    }
}

int main() {
    char x[50];
    printf("Bitte gib eine natürliche Zahl an!\n");
    scanf("%49s", x);
    printf("%s\n", x);
    int letters = strlen(x);

    

    //Teilbar durch 2?
    if (teilbar_durch_2(x) == 1) {
        printf("Ist teilbar durch 2\n");
    }
    else {
        printf("Ist nicht teilbar durch 2\n");
    }
    //Teilbar durch 3?
    if (teilbar_durch_3(x, letters) == 1) {
        printf("Ist teilbar durch 3\n");
    }
    else {
        printf("Ist nicht teilbar durch 3\n");
    }
    //Teilbar durch 4?
    if (teilbar_durch_4(x) == 1) {
        printf("Ist teilbar durch 4\n");
    }
    else {
        printf("Ist nicht teilbar durch 4\n");
    }
    //Teilbar durch 5?
    if (teilbar_durch_5(x) == 1) {
        printf("Ist teilbar durch 5\n");
    }
    else {
        printf("Ist nicht teilbar durch 5\n");
    }
    //Teilbar durch 6?
    if (teilbar_durch_6(x, letters) == 1) {
        printf("Ist teilbar durch 6\n");
    }
    else {
        printf("Ist nicht teilbar durch 6\n");
    }
    //Teilbar durch 7?
    if (teilbar_durch_7(x) == 1) {
        printf("Ist teilbar durch 7\n");
    }
    else {
        printf("Ist nicht teilbar durch 7\n");
    }
    //Teilbar durch 8?
    if (teilbar_durch_8(x) == 1) {
        printf("Ist teilbar durch 8\n");
    }
    else {
        printf("Ist nicht teilbar durch 8\n");
    }
    //Teilbar durch 9?
    if (teilbar_durch_9(x, letters) == 1) {
        printf("Ist teilbar durch 9\n");
    }
    else {
        printf("Ist nicht teilbar durch 9\n");
    }


}
