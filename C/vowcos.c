#include <stdio.h>

int main(){
    char c;
    int vc;
    printf("Enter an alphabet: ");
    scanf("%c", &c);

    vc = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');

    if (vc == 1)
        printf("%c is a vowel.", c);
    else
        printf("%c is a consonant.", c);
    return 0;
}
