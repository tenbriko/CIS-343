# Lab 2: Abstract Syntax Trees

## Expression Grammar

Breezy uses an expression grammar based on Lox.

```text
expression  → equality ;
equality    → comparison ( ( "!=" | "==" ) comparison )* ;
comparison  → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term        → factor ( ( "-" | "+" ) factor )* ;
factor      → unary ( ( "/" | "*" ) unary )* ;
unary       → ( "!" | "-" ) unary | primary ;
primary     → NUMBER | STRING | "true" | "false" | "nil"
            | "(" expression ")" ;
```

Breezy supports numbers, strings, booleans, and nil. It supports arithmetic, comparison, equality, and unary operators. The grammar is similar to Lox and uses the same operator precedence.

## AST

Breezy has four expression classes:

- `Binary` stores a left expression, operator, and right expression.
- `Unary` stores an operator and right expression.
- `Grouping` stores an expression.
- `Literal` stores a value.

## Running

No extra dependencies are needed. Run the tests from the repository folder with:

```text
python test/lab2/test_ast.py
```

## Tests

### Test 1
Purpose: Test binary, unary, grouping, and numbers.

Expected:
```text
(* (- 123) (group 45.67))
```

Actual:
```text
(* (- 123) (group 45.67))
```

Result: **PASS**

### Test 2
Purpose: Test nested arithmetic.

Expected:
```text
(+ 10 (/ 5 2))
```

Actual:
```text
(+ 10 (/ 5 2))
```

Result: **PASS**

### Test 3
Purpose: Test booleans, unary `!`, equality, and grouping.

Expected:
```text
(== (! false) (group true))
```

Actual:
```text
(== (! false) (group true))
```

Result: **PASS**

### Test 4
Purpose: Test comparison and inequality operators.

Expected:
```text
(!= (>= 10 5) (< 3 8))
```

Actual:
```text
(!= (>= 10 5) (< 3 8))
```

Result: **PASS**

### Test 5
Purpose: Test subtraction, comparison, and nil.

Expected:
```text
(> (- 10 4) (<= 3 nil))
```

Actual:
```text
(> (- 10 4) (<= 3 nil))
```

Result: **PASS**

### Test 6
Purpose: Test a string literal.

Expected:
```text
Hello Breezy
```

Actual:
```text
Hello Breezy
```

Result: **PASS**

## Known Limitations

Breezy only creates and prints hard-coded ASTs. Parsing and execution are not implemented yet.