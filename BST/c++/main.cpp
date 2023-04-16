#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip>
#include "tree.cpp"

std::vector<int> get_add_numbers(){
    std::vector<int> numbers;
    std::ifstream input_file("/datasets/add.txt");
    int number;
    while (input_file >> number) { 
        numbers.push_back(number);
    }
    input_file.close();
    return numbers;
}

std::vector<int> get_check_numbers(){
    std::vector<int> numbers;
    std::ifstream input_file("/datasets/check.txt");
    int number;
    while (input_file >> number) { 
        numbers.push_back(number);
    }
    input_file.close();
    return numbers;
}

double get_avg(int* numbers){
    int sum = 0;
    for(int i = 0; i<3;i++){
        sum += numbers[i];
    }
    double avg = (double)sum / 3 / 1000000;
    return avg;
}

int main() {
    int add_results[3];
    int check_results[3];
    int len_results[3];
    int height_results[3];
    
    std::vector<int> add_numbers = get_add_numbers();
    std::vector<int> check_numbers = get_check_numbers();

    for (int i = 0; i < 3; i++) {
        Tree* tree = new Tree();

        // Add elements to tree
        auto start = std::chrono::high_resolution_clock::now();
        for (int value : add_numbers) {
            tree->add(value);
        }
        auto stop = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        add_results[i] = static_cast<int>(duration.count());

        // Len elements
        start = std::chrono::high_resolution_clock::now();
        int length = tree->length();
        stop = std::chrono::high_resolution_clock::now();
        duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        len_results[i] = static_cast<int>(duration.count());
        std::cout << "Lenght=" << length << std::endl;

        // height elements
        start = std::chrono::high_resolution_clock::now();
        int height = tree->height();
        stop = std::chrono::high_resolution_clock::now();
        duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        height_results[i] = static_cast<int>(duration.count());
        std::cout << "Height=" << height << std::endl;

        // Check elements
        start = std::chrono::high_resolution_clock::now();
        for (int value : check_numbers) {
            tree->contain(value);
        }
        stop = std::chrono::high_resolution_clock::now();
        duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        check_results[i] = static_cast<int>(duration.count());
        delete tree;
    }



    std::cout << "Average add: " << std::fixed << std::setprecision(2) << get_avg(add_results) << std::endl;
    std::cout << "Average check: " << std::fixed << std::setprecision(2) << get_avg(check_results) << std::endl;
    std::cout << "Average len: " << std::fixed << std::setprecision(2) << get_avg(len_results) << std::endl;
    std::cout << "Average height: " << std::fixed << std::setprecision(2) << get_avg(height_results) << std::endl;
   
    return 0;
}
