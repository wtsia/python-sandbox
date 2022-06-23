# Overview
[Neetcode](https://neetcode.io/)

## Contains Duplicates
given an integer array nums, return true if any value appears at least twice

## Fizzbuzz
Description: Given some array, iterate through the array and upon chosen conditions, print fizzbuzz

# Python Basics

### `//` (divide and floor)

Divide x by y and round the answer down to the nearest integer value. Note that if one of the values is a float, you'll get back a float.
13 // 3 gives 4
-13 // 3 gives -5
9//1.81 gives 4.0

### `%` (modulo)

Returns the remainder of the division
13 % 3 gives 1. -25.5 % 2.25 gives 1.5.

### `<<` (left shift)

Shifts the bits of the number to the left by the number of bits specified. (Each number is represented in memory by bits or binary digits i.e. 0 and 1)
2 << 2 gives 8. 2 is represented by 10 in bits.
Left shifting by 2 bits gives 1000 which represents the decimal 8.

### `>>` (right shift)

Shifts the bits of the number to the right by the number of bits specified.
11 >> 1 gives 5.
11 is represented in bits by 1011 which when right shifted by 1 bit gives 101which is the decimal 5.

### `&` (bit-wise AND)

Bit-wise AND of the numbers: if both bits are 1, the result is 1. Otherwise, it's 0.
5 & 3 gives 1 (0101 & 0011 gives 0001)

### `|` (bit-wise OR)

Bitwise OR of the numbers: if both bits are 0, the result is 0. Otherwise, it's 1.
5 | 3 gives 7 (0101 | 0011 gives 0111)

### `^` (bit-wise XOR)

Bitwise XOR of the numbers: if both bits (1 or 0) are the same, the result is 0. Otherwise, it's 1.
5 ^ 3 gives 6 (O101 ^ 0011 gives 0110)

### `~` (bit-wise invert)

The bit-wise inversion of x is -(x+1)
~5 gives -6. More details at http://stackoverflow.com/a/11810203