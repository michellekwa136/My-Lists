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
