#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "tree.h"
#include "node.h"

int* read_numbers_from_file(const char* filename, int amount) {
    int* numbers = (int*)malloc(amount * sizeof(int)); // przydzielenie pamięci dla tablicy
    int i = 0;

    FILE* input_file = fopen(filename, "r"); // otwarcie pliku tekstowego

    if (input_file == NULL) {
        printf("Blad: Nie udalo sie otworzyc pliku!");
        exit(1);
    }

    while (fscanf(input_file, "%d", &numbers[i]) != EOF && i < amount) { // odczytaj liczby z pliku i zapisz w tablicy
        i++;
    }

    fclose(input_file); // zamknięcie pliku

    return numbers;
}

double get_avg(int* numbers){
    int sum = 0;
    for(int i = 0; i<3;i++){
        sum += numbers[i];
    }
    double avg = (double)sum / 3;
    return avg;
}

int main(int argc, char *argv[]) {

    int amount = atoi(argv[1]); 
   
    
    int* add_numbers = read_numbers_from_file("/datasets/add.txt", amount);
    int* check_numbers = read_numbers_from_file("/datasets/check.txt", amount);
    
    clock_t start, end;

    struct Tree* tree = new_tree();

    // Add elements to tree
    start = clock();
    for(int j=0;j<amount;j++){
        tree_add(tree, add_numbers[j]);
    }
    end = clock();
    printf("ADD_TEST: %f\n", ((double) (end - start)) / CLOCKS_PER_SEC);

    // Check elements
    start = clock();
    for(int j=0;j<amount;j++){
        tree_contain(tree, check_numbers[j]);
    }
    end = clock();
    printf("CHECK_TEST: %f\n", ((double) (end - start)) / CLOCKS_PER_SEC);

    // Len elements
    start = clock();
    for(int i=0;i<10;i++) tree_length(tree);
    end = clock();
    printf("LEN_TEST: %f\n", ((double) (end - start)) / CLOCKS_PER_SEC / 10);

    // height elements
    start = clock();
    for(int i=0;i<10;i++) tree_height(tree);
    end = clock();
    printf("HEIGHT_TEST: %f\n", ((double) (end - start)) / CLOCKS_PER_SEC / 10);

    printf("VALIDATION:%d:%d\n", tree_length(tree), tree_height(tree));

    return 0;
}
