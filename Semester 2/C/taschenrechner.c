#include <stdio.h>
#include <string.h>

int main() {
    char term[10];

    printf("Gib einen Term mit maximal 10 Zeichen ein. Nutze ausschließlich * und +: ");
    scanf("%d", &term);

    char *parts = strtok(term, "+");
    printf(*parts);

    char *subparts = strtok(*parts, "*");
    printf(*subparts);
    return 0;
}