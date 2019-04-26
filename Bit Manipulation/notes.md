# Bit Manipulation

**NOTE:** This is not my own work, the original post was found [here](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/88697). I'm copying that post here, just for my own reference.

## Background

Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a word. Computer programming tasks that require bit manipulation include low-level device control, error detection and correction algorithms, data compression, encryption algorithms, and optimization. For most other tasks, modern programming languages allow the programmer to work directly with abstractions instead of bits that represent those abstractions. Source code that does bit manipulation makes use of the bitwise operations: AND, OR, XOR, NOT, and bit shifts.

Bit manipulation, in some cases, can obviate or reduce the need to loop over a data structure and can give many-fold speed ups, as bit manipulations are processed in parallel, but the code can become more difficult to write and maintain.

## Basic

At the heart of bit manipulation are the bit-wise operators `&` (and), `|` (or), `~` (not) and `^` (exclusive-or, xor) and shift operators `a << b` and `a >> b`.

> There is no boolean operator counterpart to bitwise exclusive-or, but there is a simple explanation. The exclusive-or operation takes two inputs and returns a 1 if either one or the other of the inputs is a 1, but not if both are. That is, if both inputs are 1 or both inputs are 0, it returns 0. Bitwise exclusive-or, with the operator of a caret, ^, performs the exclusive-or operation on each pair of bits. Exclusive-or is commonly abbreviated XOR.

### Tricks

+ Set union `A | B`
+ Set intersection `A & B`
+ Set subtraction `A & ~B`
+ Set negation ALL_BITS `^A` or `~A`
+ Set bit `A |= 1 << bit`
+ Clear bit `A &= ~(1 << bit)`
+ Test bit `(A & 1 << bit) != 0`
+ Extract last bit `A & -A` or `A & ~(A-1)` or `x ^ (x & (x-1))`
+ Remove last bit `A & (A-1)`
+ Get all 1-bits `~0`

### Examples

Count the number of ones in the binary representation of the given number

```python

```

