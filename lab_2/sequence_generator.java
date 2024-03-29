package lab_2;

import java.util.Random;

/**
 * A class to generate a random binary sequence of specified length.
 */
public class sequence_generator {
    /**
     * Generates a random binary sequence of specified length.
     * 
     * @param length the length of the binary sequence to generate
     */
    public static void generateRandomSequence(int length) {
        Random random = new Random();
        for (int i = 0; i < length; ++i) {
            System.out.print(random.nextInt(2));
        }
    }

    /**
     * Main method to demonstrate the usage of {@code generateRandomSequence} method with sequence lenght = 128.
     * 
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        int sequenceLength = 128;
        generateRandomSequence(sequenceLength);
    }
}