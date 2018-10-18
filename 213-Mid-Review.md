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

- Currently running program info
  - Temporary data: %rax
  - Location of runtime stack top: %rsp
  - Location of code control point (program counter): %rip
  - Status of recent ops: CF, ZF, SF, OF
- Condition codes
  - Implicitly set (side effect of ops)
  - Single bit registers
  - CF: carry flag (for unsigned) if carry/borrow from MSB
  - ZF: zero flag if test == 0
  - SF: sign flag (for signed) if test < 0
  - OF: overflow flag (for signed) if 2's complement overflows
  - Explicit setting by 'testq'
    - Often use: testq %rax, %rax

```
cmpq b, a (like a - b)
testq b, a (like a & b)
```

- Condition codes (cont.)
  - Explicit reading by 'set' instructions
    - Set lowest byte to 0 or 1
    - Does NOT alter remaining 7 bytes

```
      Condition           Description         Jump
      ---------           -----------         ----
sete    ZF                Equal/Zero          je
setne   ~ZF               Not Equal/Zero      jne
sets    SF                Negative            js
setns   ~SF               Non-negative        jns
setg  ~(SF^OF)&~ZF        Greater             jg
setge ~(SF^OF)            Greater or Equal    jge
setl    SF^OF             Less                jl
setle   (SF^OF)|ZF        Less or Equal       jle
seta    ~CF&~ZF           Above (unsigned)    ja
setb    CF                Below (unsigned)    jb
        1                 Unconditional       jmp
```

- Why use conditional moves
  - Branching disrupts instruction flow
  - Conditional moves do not require control transfer
- Why not to use conditional moves
  - When computations are hard (both values computed)
  - When unsafe/risky computation e.g. pointer dereference
  - When computation has side effects

### Machine Programming: Procedures

- Mechanism
  - Passing control
    - To beginning of procedure code
    - Back to return point
  - Passing data
    - Arguments
    - Return value
  - Memory
    - Allocate during execution
    - Deallocate upon return
- Stack
  - Array of bytes
  - Stack pointer %rsp (stack top)
  - Grows down (towards lower value addresses)

```
pushq src
  - Fetch operand at src
  - Decrement %rsp by 8
  - Write fetched value at address in %rsp

popq dest
  - Read value at address in %rsp
  - Increment %rsp by 8
  - Store read value at dest
  - Note: stack memory does not change (only value of %rsp)
```

- Procedure control flow
  - Use stack to support call and return
  - Procedure call: 'call label'
    - Push return address on stack top
    - Jump to label
  - Return address: address of next instruction after call
  - Procedure return: 'ret'
    - Pop address from stack top
    - Jump to popped address
- Procedure data flow
  - First 6 arguments: %rdi, %rsi, %rdx, %rcx, %r8, %r9
  - More arguments on stack
  - Return value: %rax
- Stack-based languages
  - Support recursion
  - Multiple simultaneous instances of single procedure
  - Need place store state of each instance
  - Stack allocated in frames: state for single instance
- Stack frames
  - Contents: return info, local storage, temporary space (if necessary)
  - (optional) Frame pointer: %rbp
  - Stack pointer: %rsp
  - Space allocated when enter procedure, deallocated when return

```
|               |
|               |
|               |
|---------------|
|     args 7+   |   caller
|---------------|   frame
|   ret addr    |
|---------------|--------------------
|   old %rbp    | <- %rbp (optional)
|---------------|
|   saved regs  |
|       +       |
|   local vars  |
|---------------|
|   args next   | (optional)
 ---------------  <- %rsp
```

- Register saving conventions
  - "Caller saved": caller saves temporary values in frame before call
  - "Callee saved": callee saves temporary values in frame before use
    - Callee restores after use, before return to caller

```
%rax - return value, caller saved, can modify
%rdi to %r9 - arguments, caller saved, can modify
%r10, %r11 - caller saved, can modify
----------------------------------------
%rbx, %r12, %r13, %r14 - callee saved, must restore
%rbp - maybe frame pointer, callee saved, must restore
%rsp - stack pointer, callee saved, must restore when return
```

- Recursion handled by normal calling convention
  - Register saving convention prevents data corruption (unless buffer overflow)

### Machine Programming: Data

- Array allocation
  - Contiguous region in memory
  - Multidimensional: row-major ordering
  - Multi-level array
    - Must do two memory reads for access, first row array, then element
- Structure
  - Block of memory big enough to hold all fields
  - Fields ordered according to declaration
  - Compiler decides size and position of fields
- Alignment principles
  - Primitive data types requires B bytes
    - Address must be multiple of B
  - Memory access in chunks of 4 or 8 bytes
    - Inefficient if data span cache lines
    - Virtual memory trickier if data span two pages
  - Compiler inserts gaps (paddings) in structure to ensure correct alignment of fields
- Structure alignment
  - Within structure: must satisfy each element's alignment
  - Overall: structure must align at largest alignment requirement in structure
  - Internal & external paddings
  - Saving space: put large data types first
- Floating points
  - Arguments in %xmm0, %xmm1,...
  - Return value in %xmm0
  - All XMM registers are caller saved
  - Different mov instructions
  - Lots of different instructions
  - Set condition codes ZF, PF, CF
  - PF: parity flag

### Machine Programming: Advanced Topics

- Memory layout
  - Shared library
  - Stack (grow down, at most 8 MB)
  - Heap (grow up)
  - Data (globals, statics, string consts, etc.)
  - Text: executable code, read-only
- Buffer overflow
  - Exceed memory size allocated
  - #1 technical cause of security vulnerabilities
  - Most common: unchecked length of string inputs (particularly stack smashing)
- What to do about buffer overflow attacks
  - Avoid overflow vulnerabilities
    - Use library routines that limit string length
  - System-level protection
    - Randomized stack offset
    - Mark stack non-executable
  - Stack canaries
    - Place special values on stack beyond buffer
    - Check for value corruption before exiting
- Return-oriented attacks
  - Use existing code
  - Does not overcome stack canaries
  - Construct program from gadgets
- Union allocation
  - Allocate according to largest element
  - Can only use one field at a time

### Code Optimization
