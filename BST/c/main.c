#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "tree.h"
#include "node.h"
#define MAX_SIZE 10000000

int* read_numbers_from_file(char* filename, int* size) {
    int* numbers = (int*)malloc(MAX_SIZE * sizeof(int)); // przydzielenie pamięci dla tablicy
    int i = 0;

    FILE* input_file = fopen(filename, "r"); // otwarcie pliku tekstowego

    if (input_file == NULL) {
        printf("Blad: Nie udalo sie otworzyc pliku!");
        exit(1);
    }

    while (fscanf(input_file, "%d", &numbers[i]) != EOF && i < MAX_SIZE) { // odczytaj liczby z pliku i zapisz w tablicy
        i++;
    }

    fclose(input_file); // zamknięcie pliku

    *size = i; // ustawienie liczby elementów w tablicy

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

int main() {
    int add_results[3];
    int check_results[3];
    int len_results[3];
    int height_results[3];
    
    int add_numbers_size;
    int* add_numbers = read_numbers_from_file("/datasets/add.txt", &add_numbers_size);
    int check_numbers_size;
    int* check_numbers = read_numbers_from_file("/datasets/check.txt", &check_numbers_size);
    
    clock_t start, end;
    double cpu_time_used;

    for(int i=0;i<3;i++){
        struct Tree* tree = new_tree();

        // Add elements to tree
        start = clock();
        for(int j=0;j<add_numbers_size;j++){
            tree_add(tree, add_numbers[j]);
        }
        end = clock();
        add_results[i] = ((double) (end - start)) / CLOCKS_PER_SEC;

        // Len elements
        start = clock();
        int length = tree_length(tree);
        end = clock();
        len_results[i] = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Length=%d\n", length);

        // height elements
        start = clock();
        int height = tree_height(tree);
        end = clock();
        height_results[i] = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Height=%d\n", height);

        // Check elements
        start = clock();
        for(int j=0;j<check_numbers_size;j++){
            tree_contain(tree, check_numbers[j]);
        }
        end = clock();
        check_results[i] = ((double) (end - start)) / CLOCKS_PER_SEC;
    }

    printf("Average add: %.4f\n", get_avg(add_results));
    printf("Average check: %.4f\n", get_avg(check_results));
    printf("Average len: %.4f\n", get_avg(len_results));
    printf("Average height: %.4f\n", get_avg(height_results));

    return 0;
}
