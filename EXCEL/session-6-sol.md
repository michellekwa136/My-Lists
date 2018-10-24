This is a brief solution manual for EXCEL session 6, Fall 2018.

---

### 1. RSA Review

```
p = 3, q = 7
n = pq = 21
\varphi(n) = (p - 1)(q - 1) = 12
(n, e) = (21, 5)
de \equiv 1 mod \varphi(n) => 5d \equiv 1 mod 12 => d \equiv 5 mod 12 => (n, d) = (21, 5)
K \equiv M^e mod n => K \equiv 2^5 mod 21 => K = 11
M \equiv K^d mod n => M \equiv 11^5 mod 21 => M = 2
```

### Puzzle 001

```
(4)(7) + 9 - 13 = 24
(4)(13 - 10) + 12 = 24
```

### 2. Euclidean Algo Review

```
gcd(150, 216) = 6.
```

### 3. Function Diagnosis

```
a) f is not well-defined, domain needs to be restricted, codomain is fine
b) g is not well-defined, violates uniqueness due to g(x) = 0 and 1 for any x, codomain needs to be restricted
```

### 4. Definitions Review

See Clive Notes.

### Puzzle 002

Inscribe a unit circle in a square of length 2 units. Inscribe a unit hexagon in the circle. Areas of hexagon, circle, and square are 3, PI, 4 respectively.

### 5. Elementary Functions

```
a) f1 is bijective
b) f2 is not injective, not surjective, complete the square to prove
c) f3 is injective, not surjective, no value 0
d) f4 is injective, not surjective (ignore injective proof)
e) g first find specification, then try inverse
```

### 6. From Stars to Dots to Stars

```
a) f has no right inverse due to not surjective
b) g has no left inverse due to not injective
c) h has no left inverse (ignore computing right inverse)
```

### 7. Piece it together

```
(\mathbb{Z}, +)
- closure: yes
- associative: yes
- identity: 0
- inverse: \forall x \in \mathbb{Z}, -x is inverse

(F, o)
- closure: compose and expand, claim a' and b' exist in domain
- associative: yes - pure algebra
- identity: f1,0
- inverse: f1/a,-b/a
```
