#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip>
#include "tree.cpp"

std::vector<int> get_add_numbers(int amount){
    std::vector<int> numbers;
    std::ifstream input_file("/datasets/add.txt");
    int number;
    while (input_file >> number) { 
        numbers.push_back(number);
    }
    input_file.close();
    return std::vector<int>(numbers.begin(), numbers.begin() + amount);
}

std::vector<int> get_check_numbers(int amount){
    std::vector<int> numbers;
    std::ifstream input_file("/datasets/check.txt");
    int number;
    while (input_file >> number) { 
        numbers.push_back(number);
    }
    input_file.close();
    return std::vector<int>(numbers.begin(), numbers.begin() + amount);
}


int main(int argc, char* argv[]) {

    int amount = std::stoi(argv[1]);
    
    std::vector<int> add_numbers = get_add_numbers(amount);
    std::vector<int> check_numbers = get_check_numbers(amount);

    
    Tree* tree = new Tree();

    // Add elements to tree
    auto start_add = std::chrono::high_resolution_clock::now();
    for (int value : add_numbers) {
        tree->add(value);
    }
    auto stop_add = std::chrono::high_resolution_clock::now();
    auto duration_add = 1.0 * std::chrono::duration_cast<std::chrono::microseconds>(stop_add - start_add).count();
    std::cout << "ADD_TEST:" << duration_add/1000000.0 << std::endl;

    // Check elements
    auto start_check = std::chrono::high_resolution_clock::now();
    for (int value : add_numbers) {
        tree->contain(value);
    }
    auto stop_check = std::chrono::high_resolution_clock::now();
    auto duration_check = 1.0 * std::chrono::duration_cast<std::chrono::microseconds>(stop_check - start_check).count();
    std::cout << "CHECK_TEST:" << duration_check/1000000.0 << std::endl;

    // Len elements
    auto start_len = std::chrono::high_resolution_clock::now();
    for (int i=0;i<10;i++) int length = tree->length();
    auto stop_len = std::chrono::high_resolution_clock::now();
    auto duration_len = 1.0 * std::chrono::duration_cast<std::chrono::microseconds>(stop_len - start_len).count();
    std::cout << "LEN_TEST:" << duration_len/1000000.0/10.0 << std::endl;

    // height elements
    auto start_h = std::chrono::high_resolution_clock::now();
    for (int i=0;i<10;i++) int length = tree->height();
    auto stop_h = std::chrono::high_resolution_clock::now();
    auto duration_h = 1.0 * std::chrono::duration_cast<std::chrono::microseconds>(stop_h - start_h).count();
    std::cout << "HEIGHT_TEST:" << duration_h/1000000.0/10.0 << std::endl;

    std::cout << "VALIDATION:"<<tree->length()<<":"<<tree->height()<< std::endl;

    delete tree;
  
    return 0;
}
