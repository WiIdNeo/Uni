int teilbar_durch_2(char x[]) {
    if (((int)x[-1]%2) == 0) {
        return 1;
    }
    else {
        return 0;
    }
}
int teilbar_durch_3(char x[]) {
    int y = 0;
    char* endptr;
    int letters = sizeof(x) / sizeof(x[0]);
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
int teilbar_durch_4(char x[]) {
    if (((int)x[-2]%4) == 0) {
        return 1;
    }
    else {
        return 0;
    }
}
int teilbar_durch_5(char x[]) {
    if ((int)x[-1] == 0 || (int)x[-1] == 5) {
        return 1;
    }
    else {
        return 0;
    }
}
int teilbar_durch_6(char x[]) {
    if (teilbar_durch_2(x) == 1 && teilbar_durch_3(x) == 1) {
        return 1;
    }
    else{
        return 0;
    }
}
int teilbar_durch_7(char x[]) {
    int rest = (int)x;
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
int teilbar_durch_8(char x[]) {
    if (((int)x[-3]%8) == 0) {
        return 1;
    }
    else {
        return 0;
    }
}
int teilbar_durch_9(char x[]) {
    int y = 0;
    char* endptr;
    int letters = sizeof(x) / sizeof(x[0]);
    do{
      for (int i = 0; i < letters; i++) {
        y = y+(int)x[i];
    }  
    } while (y > 9);
    if (y==9) {
        return 1;
    }
    else{
        return 0;
    }
}
