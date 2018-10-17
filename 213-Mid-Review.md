# 15213 Midterm Review

---

Summary and Key Concepts from Lecture Slides

### Bits, Bytes, Integers (Part I)

- Why use bits?
  - Easy to store with bi-stable elements
  - Reliable in transfer
- Byte = 8 bits
  - 1 byte: 00000000 to 11111111 in binary
  - 1 byte: 0 to 255 in decimal
  - 1 byte: 00 to FF in hex
- Data representation in C (32 vs. 64)
  - char = 1, 1
  - short = 2, 2
  - int = 4, 4
  - long = 4, 8
  - float = 4, 4
  - double = 8, 8
  - pointer = 4, 8
  - size_t = \_, 8
- Encode "true" as 1 and "false" as 0 (boolean algebra)
  - And '&'
  - Or '|'
  - Xor '^'
  - Not '~'
- Bit-level operations in C
  - Apply to: long, int, short, char, unsigned

```
Hex Dec Bin  | Hex Dec Bin
--- --- ---  | --- --- ---
  0   0 0000 |   8   8 1000
  1   1 0001 |   9   9 1001
  2   2 0010 |   A  10 1010
  3   3 0011 |   B  11 1011
  4   4 0100 |   C  12 1100
  5   5 0101 |   D  13 1101
  6   6 0110 |   E  14 1110
  7   7 0111 |   F  15 1111
```

- Logic operations in C ('&&', '||', '!')
  - View 0 as False, anything non-zero True
  - Always return 0 or 1
- Left shift: x << y
  - Throw away bits on left
  - Fill 0's on right
- Right shift: x >> y
  - Throw away bits on right
  - 2 types
    - Logical: Fill 0's on left
    - Arithmetic: Replicate MSB on left
- Shift amount < 0 or >= word size: Undefined

```
Two's Complement Representation of Signed
    -16 8  4  2  1
 10: 0  1  0  1  0 = 8 + 2 = 10
-10: 1  0  1  1  0 = -16 + 4 + 2 = -10
```

- Range
  - Unsigned: 0 to 2^w-1
  - Signed: -2^(w-1) to 2^(w-1)-1
  - Observations
    - |Tmin| = Tmax + 1
    - Umax = 2Tmax + 1
- Casting between signed and unsigned: keep bit representation, re-interpret
  - Observation: large negative weight becomes large positive weight
  - Positives: no change
  - Negatives: all shift up to big positives
- Conventions in C
  - Constants: default as signed integers
  - Has implicit castings
  - Signed always implicitly cast to unsigned, not the reverse
- Sign extension: make k copies of MSB (from smaller to larger type - automatic extension)
- Truncation: simply drop top k bits (similar to mod operation)

### Bits, Bytes, Integers (Part II)

- Unsigned addition: discard carry bit (modular arithmetic)
  - Wraps around at most once
- Signed: same bit-level behavior
  - Discard carry bit
  - Drop MSB, re-interpret
  - Wraps around positive or negative at most once
- Multiplication
  - Ignore higher bits
  - Modular arithmetic
  - Shift is faster than multiply (compiler optimize)
  - Unsigned right shift divide: logical shift
  - Signed right shift divide: arithmetic shift

```
Negation = Complement & Increment
  ~x + 1 == -x
Counterexample: Tmin
```

```
Proper way to use Unsigned as Loop Index
  unsigned i
  for (i = cnt - 2; i < cnt; i--)
    ...
```

- Why use unsigned 
  - When perform modular arithmetic (guaranteed)
  - When use bits to represent sets
  - Use in system (bit mask, etc.)
- System provides private address space for each process
- Word size: 64-bit = 8 bytes per word
- Memory organization is word-oriented
- Byte ordering conventions
  - Big endian: LSB in highest address
  - Little endian: LSB in lowest address

```
Representing a 4-byte value 0x01234567
                0x100 0x101 0x102 0x103 -> higher addresses
Big Endian:     01    23    45    67
Little Endian:  67    45    23    01
```

- Strings in C
  - Array of chars
  - Each char encoded in ASCII
  - Null-terminated: final character '00'
  - Byte ordering no affect

```
Read reversed string from Assembly
  add $0x12ab, %ebx
1. asm value = 0x12ab
2. pad to 32 bits = 0x000012ab
3. split into bytes = 00 00 12 ab
4. reverse = ab 12 00 00
```

### Floating Point

- Fractional binary: bits to right of "binary point" represent fractional power of 2
  - Represent some rational numbers
- Observations
  - Divide by 2 = shift right
  - Multiply by 2 = shift left
- IEEE Standard 754
  - Nice standards for rounding, overflow, underflow
  - Hard to make fast in hardware
- (-1)^s M 2^E
  - s: sign bit
  - M: significand, normally a fraction between 1 to 2 (exclude 2)
  - E: exponent
  - Encoding = |s|exp|frac|
    - s is sign bit
    - exp encodes but not equal to E
    - frac encodes but not equal to M
- Precision
  - Single: 32 bits = 1 s + 8 exp + 23 frac
  - Double: 64 bits = 1 s + 11 exp + 52 frac
- Three "kinds" of floating points: denormalized, normalized, special
- Normalized
  - when exp != 00..0 or 11..1
  - E = exp - Bias
    - Single precision: 127
    - Double precision: 1023
  - M = 1.frac
- Denormalized
  - when exp == 00..0
  - E = 1 - Bias
  - M = 0.frac
  - If frac == 00..0: represent zeros (signed)
  - If frac != 00..0: numbers closest to zeros
- Special values
  - when exp == 11..1
  - If frac == 00..0: represent infinity (signed) (due to overflow)
  - If frac != 00..0: Not-a-Number (NaN) (due to undefined arithmetic)

```
|---|---|----------|-------|||-------|----------|---|---|
 NaN Inf   -Norm.    -Den. -+0 +Den.    +Norm.   Inf NaN
```

- Rounding: to nearest even (default)
- BB-G-R-XXX
  - G: guard bit = LSB of result
  - R: round bit = 1st bit removed
  - XXX: sticky bits
- Round-up conditions
  - R = 1, S = 1xx (>0.5) round to nearest
  - G = 1, R = 1, S = 0 round to even
- Fixings of multiplication
  - If M >= 2: right shift M, increment E
  - If E out of range: overflow!
- Fixings of addition
  - If M >= 2: right shift M, increment E (same above)
  - If M < 1: left shift M k positions, decrement E by k
  - If E out of range: overflow!
- Properties of FP addition
  - Closed under addition (but may give Inf or NaN)
  - Commutative
  - NOT associative
  - 0 is identity
- Properties of FP multiplication
  - Closed under multiplication (but may give Inf or NaN)
  - Commutative
  - NOT associative
  - 1 is identity
  - NOT distribute over addition
- Casting between int, float, double: change bit representation
  - float/double to int: truncate frac
  - int to double: exact conversion if int <= 53 bit
  - int to float: round

### Machine Programming: Basics

- Architecture: parts of processor design needed for correct machine/assembly code
  - Machine code: byte-level executable
  - Assembly code: text representation of machine code

```
movq src, dest
  1. immediate values e.g. $0x400
  2. register e.g. %rax
  3. 8 bytes of memory e.g. (%rax)
```

```
Memory Addressing Modes
- Normal (R) direct access register R specified location
- Displacement D(R) R specified location with displacement D offset
- General Form D(Rb, Ri, S) = [Rb] + S * [Ri] + D
```

```
leaq src, dest - set dest to address denoted by src
addq
subq
imulq
salq (left arithmetic shift)
sarq (right arithmetic shift)
shrq (right logical shift)
xorq
andq
orq
incq dest
decq dest
negq dest
notq dest
```

- Turn C into Object Code
  - gcc -Og ...c ...c -o p
    - Og = basic optimization
    - p is result binary

```
text (C) -----> text (asm) -----> binary (o) -----> binary (executable)
         compiler          assembler         linker
```

- Assembler
  - Translate .s to .o
  - Encode instructions in binary
  - Nearly complete image of executable
  - Missing linkage between diff files
- Linker
  - Resolves references between files
  - Combines static runtime libraries
  - Some libraries dynamically linked
- Disassembler
  - objdump -d ...
  - Useful for examining object code
  - Produce approximate of assembly code
  - can run on both .o and executable

```
Using GDB
- disassemble ...
```

### Machine Programming: Control
