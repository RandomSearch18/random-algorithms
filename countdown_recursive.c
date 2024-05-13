// gcc -O1 -foptimize-sibling-calls countdown_recursive.c -o countdown

#include <stdio.h>

void countdown(int number) {
    if (number == 0) {
        return;
    }
    printf("%d\n", number);
    countdown(number - 1);
}

int main() {
    countdown(10000000);
    return 0;
}