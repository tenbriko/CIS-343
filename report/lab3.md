# Lab 3: Parsing

## Grammar

Breezy uses the same expression grammar as Lab 2.

```text
expression → equality ;
equality → comparison ( ( "!=" | "==" ) comparison )* ;
comparison → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term → factor ( ( "+" | "-" ) factor )* ;
factor → unary ( ( "*" | "/" ) unary )* ;
unary → ( "!" | "-" ) unary | primary ;
primary → NUMBER | STRING | "true" | "false" | "nil"
        | "(" expression ")" ;
```

Breezy follows Lox's operator precedence. Multiplication and division happen before addition and subtraction. Binary operators are left-associative, and unary operators are right-associative. The grammar did not change from Lab 2.

## Design

I reused my scanner, AST classes, and printer from the previous labs. I added a parser to turn tokens into an AST.

Breezy is similar to Lox, but uses my own language design. I added `nil` support and error checking.

## Running

No extra packages are needed.

Interactive mode: `python src/breezy.py`

File mode: `python src/breezy.py test/lab3/valid.bzy`

## Tests

I tested the parser using different expressions and errors. All expected outputs matched the actual outputs.

| Test | Input | Expected and actual output | Result |
|---|---|---|---|
| Precedence | `10 + 5 * 2` | `(+ 10.0 (* 5.0 2.0))` | PASS |
| Missing operand | `10 +` | `[line 1] Error at end: Expected expression.` | PASS |
| Missing parenthesis | `(10 + 5` | `[line 1] Error at end: Expected ')' after expression.` | PASS |
| Extra tokens | `10 20` | `[line 1] Error at '20': Unexpected token after expression.` | PASS |
| Invalid character | `10 @ + 5` | `[line 1] Error: Unexpected character '@'.` | PASS |
| Unclosed string | `"Hello` | `[line 1] Error: Unterminated string.` | PASS |
| Interactive recovery | `10 + 5` after an error | `(+ 10.0 5.0)` | PASS |

I also tested `operators.bzy` and `literals.bzy`. Both printed the correct AST.

The errors happened because an expression was incomplete, a parenthesis was missing, extra tokens were entered, or invalid characters were used.

### Operators Test

Input file: `test/lab3/operators.bzy`

Expected output:

```text
(!= (== (!= (== (group (>= 10.0 5.0)) (group (< 3.0 8.0))) (group (<= 7.0 9.0))) (group (> 4.0 2.0))) (group (+ (- 10.0 3.0) (/ (* 2.0 4.0) 2.0))))
```

Actual output: Same as expected.

Result: PASS

### Literals Test

Input file: `test/lab3/literals.bzy`

Expected output:

```text
(== (!= (group (== (! false) true)) (group (== Hello Breezy nil))) (group (< (- 5.0) 0.0)))
```

Actual output: Same as expected.

Result: PASS

## Syntax Tree

Expression: `10 + 5 * 2`

```text
expression
└── equality
    └── comparison
        └── term
            ├── factor → unary → primary → 10
            ├── +
            └── factor
                ├── unary → primary → 5
                ├── *
                └── unary → primary → 2
```

Printed AST:

```text
(+ 10.0 (* 5.0 2.0))
```

The tree shows that multiplication happens before addition.

## Known Limitations

Breezy only parses expressions. It does not run code or support statements yet.