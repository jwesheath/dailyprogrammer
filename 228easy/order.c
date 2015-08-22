#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int is_ordered(char* word);
int is_reverse_ordered(char* word);
char* output_message(char* word);

int main(int argc, char* argv[]) {

    if (argc != 2) {
        printf("Must provide text file as only command line argument!\n");
    }

    FILE* infile = fopen(argv[1], "r");

    if (infile) {
        char line[80];
        while(fgets(line, 80, infile)) {    
            // Strip the \n from the end of the word
            char word[strlen(line) - 1];            
            for (int i = 0; i < strlen(line) - 1; i++) {
                word[i] = line[i];
            }
            printf("%s %s\n", word, output_message(word));
        }
    }
    return 0;
}

int is_ordered(char* word) {
    int low = 'a';
    for (int i = 0; i < strlen(word); i++) {
        int c = tolower(word[i]);
        if (c >= low) {
            low = c;
        } else {
            return 0;
        }
    }
    return 1;
}

int is_reverse_ordered(char* word) {
    int high = 'z';
    for (int i = 0; i < strlen(word); i++) {
        int c = tolower(word[i]); 
        if (c <= high) {
            high = c;
        } else {
            return 0;
        }
    }
    return 1;
}

char* output_message(char* word) {
    if (is_ordered(word)) {
        return "IN ORDER";
    } else if (is_reverse_ordered(word)) {
        return "REVERSE ORDER";
    } else {
        return "NOT IN ORDER";
    }
}
