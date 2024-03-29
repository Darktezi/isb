/**
 * @file sequence_generator.cpp
 * @brief A program to generate a random binary sequence of specified length.
 */

#include <iostream>
#include <ctime>
#include <cstdlib>

/**
 * Generates a random binary sequence of specified length.
 *
 * @param length the length of the binary sequence to generate
 */
void generateRandomSequence(int length) {
    srand(time(NULL));
    for (int i = 0; i < length; ++i) {
        std::cout << rand() % 2;
    }
}

/**
 * Main function to demonstrate the usage of generateRandomSequence method with sequence lenght = 128.
 *
 * @return 0 on successful execution
 */
int main() {
    int sequenceLength = 128;
    generateRandomSequence(sequenceLength);
    return 0;
}