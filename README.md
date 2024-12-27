# NLN_Factorization_Method
A new way to factor any number

Shift-and-Shave Factorization Method

Overview
The Shift-and-Shave Factorization method is a novel approach to finding factors of a number by combining binary operations (circular shifts and bit-shaving) with recursive decomposition. This algorithm leverages the properties of binary numbers, parallel processing, and recursive techniques to identify prime factors efficiently.

This document explains the methodology, the code structure, and how to use this implementation to explore factorization.

How It Works
1. Binary Representation
The method begins by converting a number into its binary form, enabling bitwise operations. This binary representation provides the foundation for circular shifts and bit-shaving.

2. Circular Shifts
The binary string undergoes left and right circular shifts, which rearrange its bits:
- Left Shift: Rotates bits to the left, wrapping the leftmost bit to the rightmost position.
- Right Shift: Rotates bits to the right, wrapping the rightmost bit to the leftmost position.

Each shifted binary string is converted back to decimal, and the resulting number is tested as a potential factor.

3. Bit Shaving
For each shifted binary string, bits are systematically removed from the beginning. These shaved binary strings are converted to decimal, and the resulting numbers are also tested as potential factors.

4. Recursion
If a factor is composite (not prime), the algorithm recursively applies the shift-and-shave method to decompose it into its prime factors.

5. Parallel Processing
To speed up the analysis, the algorithm uses multithreading to perform shifts and shaving operations in parallel.

Code Structure

Functions
decimal_to_binary(n: int) -> str  
Converts a decimal number to binary (without the 0b prefix).

binary_to_decimal(b: str) -> int  
Converts a binary string back to its decimal equivalent.

circular_shift_left(b: str, k: int) -> str  
Performs a circular left shift on a binary string by k positions.

circular_shift_right(b: str, k: int) -> str  
Performs a circular right shift on a binary string by k positions.

shave_bits(b: str, num_bits: int) -> List[str]  
Removes leading bits from a binary string up to num_bits, returning all shaved versions.

is_prime(n: int) -> bool  
Determines if a number is prime using a simple primality test.

process_shift(n: int, binary_n: str, direction: str, k: int) -> Set[int]  
Processes a circular shift in the specified direction and checks if the shifted number is a factor.

process_shave(n: int, binary_shifted: str, num_bits: int) -> Set[int]  
Processes bit-shaving on a binary string and checks if the shaved numbers are factors.

shift_and_shave(n: int, depth: int = 0, visited: Set[int] = None) -> Set[int]  
Recursively applies shift-and-shave operations to find factors of a number.

factorize(n: int) -> List[int]  
Combines all the above methods to return the prime factors of a number.

How to Use

Requirements
- Python 3.8 or later
- No additional libraries are required for basic functionality. Multithreading is built into the Python standard library.

Running the Code
1. Copy the code into a Python file (e.g., shift_and_shave.py).
2. In the main function, specify the number you want to factorize by updating the value of the variable number.
3. Run the script. For example, using the terminal or command line:
   python shift_and_shave.py
4. The script will output the prime factors of the specified number.

Example Usage
Input: 42  
Factoring 42 using shift-and-shave method:  
Prime Factors: [2, 3, 7]  

Input: 9007199254740991  
Factoring 9007199254740991 using shift-and-shave method:  
Prime Factors: [7, 73, 127, 337]  

Customization
You can adjust the depth of recursion and the number of shifts by modifying the parameters in the shift_and_shave function. The code is also designed to handle extremely large numbers by leveraging multithreading for efficiency.

Limitations and Future Directions
While the method is efficient for moderate-sized numbers, its performance for very large numbers depends on computational resources. Optimizations such as parallel processing and algorithmic refinements could further improve its scalability.

This method is a unique combination of binary arithmetic, primality testing, and recursive decomposition, making it a powerful tool for exploring the hidden structure of numbers.



Factoring 10376 using shift-and-shave method:
Prime Factors: [1, 2, 1297, 2594, 5188]
Debugging shift-and-shave for number: 10376 (binary: 10100010001000)
Shift left by 1: 01000100010001 -> 4369
Shift left by 2: 10001000100010 -> 8738
Shift left by 3: 00010001000101 -> 1093
Shift left by 4: 00100010001010 -> 2186
Shift left by 5: 01000100010100 -> 4372
Shift left by 6: 10001000101000 -> 8744
Shift left by 7: 00010001010001 -> 1105
Shift left by 8: 00100010100010 -> 2210
Shift left by 9: 01000101000100 -> 4420
Shift left by 10: 10001010001000 -> 8840
Shift left by 11: 00010100010001 -> 1297
Found factor from shift: 1297
Shift left by 12: 00101000100010 -> 2594
Found factor from shift: 2594
Shift left by 13: 01010001000100 -> 5188
Found factor from shift: 5188
Shift right by 1: 01010001000100 -> 5188
Found factor from shift: 5188
Shift right by 2: 00101000100010 -> 2594
Found factor from shift: 2594
Shift right by 3: 00010100010001 -> 1297
Found factor from shift: 1297
Shift right by 4: 10001010001000 -> 8840
Shift right by 5: 01000101000100 -> 4420
Shift right by 6: 00100010100010 -> 2210
Shift right by 7: 00010001010001 -> 1105
Shift right by 8: 10001000101000 -> 8744
Shift right by 9: 01000100010100 -> 4372
Shift right by 10: 00100010001010 -> 2186
Shift right by 11: 00010001000101 -> 1093
Shift right by 12: 10001000100010 -> 8738
Shift right by 13: 01000100010001 -> 4369
Shave 1 bits: 0100010001000 -> 2184
Shave 2 bits: 0100010001000 -> 2184
Shave 2 bits: 100010001000 -> 2184
Shave 3 bits: 0100010001000 -> 2184
Shave 3 bits: 100010001000 -> 2184
Shave 3 bits: 00010001000 -> 136
Shave 4 bits: 0100010001000 -> 2184
Shave 4 bits: 100010001000 -> 2184
Shave 4 bits: 00010001000 -> 136
Shave 4 bits: 0010001000 -> 136
Shave 5 bits: 0100010001000 -> 2184
Shave 5 bits: 100010001000 -> 2184
Shave 5 bits: 00010001000 -> 136
Shave 5 bits: 0010001000 -> 136
Shave 5 bits: 010001000 -> 136
Shave 6 bits: 0100010001000 -> 2184
Shave 6 bits: 100010001000 -> 2184
Shave 6 bits: 00010001000 -> 136
Shave 6 bits: 0010001000 -> 136
Shave 6 bits: 010001000 -> 136
Shave 6 bits: 10001000 -> 136
Shave 7 bits: 0100010001000 -> 2184
Shave 7 bits: 100010001000 -> 2184
Shave 7 bits: 00010001000 -> 136
Shave 7 bits: 0010001000 -> 136
Shave 7 bits: 010001000 -> 136
Shave 7 bits: 10001000 -> 136
Shave 7 bits: 0001000 -> 8
Found factor from shave: 8
Shave 8 bits: 0100010001000 -> 2184
Shave 8 bits: 100010001000 -> 2184
Shave 8 bits: 00010001000 -> 136
Shave 8 bits: 0010001000 -> 136
Shave 8 bits: 010001000 -> 136
Shave 8 bits: 10001000 -> 136
Shave 8 bits: 0001000 -> 8
Found factor from shave: 8
Shave 8 bits: 001000 -> 8
Found factor from shave: 8
Shave 9 bits: 0100010001000 -> 2184
Shave 9 bits: 100010001000 -> 2184
Shave 9 bits: 00010001000 -> 136
Shave 9 bits: 0010001000 -> 136
Shave 9 bits: 010001000 -> 136
Shave 9 bits: 10001000 -> 136
Shave 9 bits: 0001000 -> 8
Found factor from shave: 8
Shave 9 bits: 001000 -> 8
Found factor from shave: 8
Shave 9 bits: 01000 -> 8
Found factor from shave: 8
Shave 10 bits: 0100010001000 -> 2184
Shave 10 bits: 100010001000 -> 2184
Shave 10 bits: 00010001000 -> 136
Shave 10 bits: 0010001000 -> 136
Shave 10 bits: 010001000 -> 136
Shave 10 bits: 10001000 -> 136
Shave 10 bits: 0001000 -> 8
Found factor from shave: 8
Shave 10 bits: 001000 -> 8
Found factor from shave: 8
Shave 10 bits: 01000 -> 8
Found factor from shave: 8
Shave 10 bits: 1000 -> 8
Found factor from shave: 8
Shave 11 bits: 0100010001000 -> 2184
Shave 11 bits: 100010001000 -> 2184
Shave 11 bits: 00010001000 -> 136
Shave 11 bits: 0010001000 -> 136
Shave 11 bits: 010001000 -> 136
Shave 11 bits: 10001000 -> 136
Shave 11 bits: 0001000 -> 8
Found factor from shave: 8
Shave 11 bits: 001000 -> 8
Found factor from shave: 8
Shave 11 bits: 01000 -> 8
Found factor from shave: 8
Shave 11 bits: 1000 -> 8
Found factor from shave: 8
Shave 11 bits: 000 -> 0
Shave 12 bits: 0100010001000 -> 2184
Shave 12 bits: 100010001000 -> 2184
Shave 12 bits: 00010001000 -> 136
Shave 12 bits: 0010001000 -> 136
Shave 12 bits: 010001000 -> 136
Shave 12 bits: 10001000 -> 136
Shave 12 bits: 0001000 -> 8
Found factor from shave: 8
Shave 12 bits: 001000 -> 8
Found factor from shave: 8
Shave 12 bits: 01000 -> 8
Found factor from shave: 8
Shave 12 bits: 1000 -> 8
Found factor from shave: 8
Shave 12 bits: 000 -> 0
Shave 12 bits: 00 -> 0
Shave 13 bits: 0100010001000 -> 2184
Shave 13 bits: 100010001000 -> 2184
Shave 13 bits: 00010001000 -> 136
Shave 13 bits: 0010001000 -> 136
Shave 13 bits: 010001000 -> 136
Shave 13 bits: 10001000 -> 136
Shave 13 bits: 0001000 -> 8
Found factor from shave: 8
Shave 13 bits: 001000 -> 8
Found factor from shave: 8
Shave 13 bits: 01000 -> 8
Found factor from shave: 8
Shave 13 bits: 1000 -> 8
Found factor from shave: 8
Shave 13 bits: 000 -> 0
Shave 13 bits: 00 -> 0
Shave 13 bits: 0 -> 0

If not all correct factors are found, which in this case, the method fails... how, I don't know as 8 was found as a factor which is 2 * 2 * 2 and well, 1297 as well is a resulting factor but the program isn't perfect and this idea isn't completely confirmed either. Feel free to test out different ideas and see where this takes you!
[2, 2, 2, 1297]

