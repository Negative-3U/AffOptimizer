# AffOptimizer
 This script will "optimize" your .aff file to reduce the size

## This script will:

1. Replace all `arctap` with the alias `at`.
2. Remove all unnecessary zeros in decimals.
3. Use LF line breaks and remove all unnecessary newlines.
4. Remove all useless content in header.

## Usage

```
python3 aff_optimizer.py <in.aff> <out.aff>
```

## Testing result

 Typically, this script reduces the .aff file size by about 15%:

```
ω4            2.aff: 173KB -> 143KB
Pentiment     3.aff: 106KB -> 90.3KB
Testify       3.aff: 101KB -> 87.8KB
Callima Karma 2.aff: 91.7KB -> 78.2KB

and...
10MB.aff: 10MB -> 8.31MB
```

