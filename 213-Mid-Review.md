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
