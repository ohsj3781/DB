#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "B+TREE.h"

/*
B+ Tree launcher
Refer to README.md for more information
*/

int main(int argc, char* argv[]) {
    if (argc == 1) {
        printf("Usage: %s <input file>\n", argv[0]);
        exit(1);
    }

    FILE* fp = fopen(argv[1], "r");
    if (fp == NULL) {
        perror("Error opening file");
        exit(1);
    }

    // Read instructions from file
    // Format:
    // First line states the number of degrees
    // Rest of line follows this format:
    // p: print tree
    // i <key>: insert key
    // r <key>: remove key
    int degree;
    if (fscanf(fp, " %d", &degree) != 1) {
        perror("Error reading file");
        exit(1);
    }

    printf("Degree: %d\n", degree);
    BPLUSTreeInit(degree);

    char instruction;
    int key, fscanf_result;
    while (true) {
        fscanf_result = fscanf(fp, " %c", &instruction);
        if (fscanf_result == EOF) {
            break;
        } else if (fscanf_result != 1) {
            perror("Error reading file");
            exit(1);
        }

        if (instruction == 'p') {
            printTree();
            continue;
        }

        // Read key
        if (fscanf(fp, " %d", &key) != 1) {
            perror("Error reading file");
            exit(1);
        }

        switch (instruction) {
            case 'i':
                printf("Insert %d\n", key);
                insertElement(key);
                break;
            case 'r':
                printf("Remove %d\n", key);
                removeElement(key);
                break;
            default:
                printf("Invalid instruction: %c\n", instruction);
                exit(1);
        }
    }

    fclose(fp);
    return 0;
}
