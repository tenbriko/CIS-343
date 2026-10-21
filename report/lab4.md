# Lab 4: Evaluating Expressions

## Overview

For this lab, I added an evaluator to my Breezy programming language. It takes the AST from the parser and evaluates expressions to get a result.

## Design

I created `evaluator.py` to evaluate expressions using post-order traversal. This means it evaluates the child expressions before applying the operator.

I reused my scanner, parser, and AST classes from the previous labs.

Breezy supports arithmetic, comparisons, equality, unary operators, and string concatenation.

## Evaluation Rules

- Numbers are stored as floats.
- Only `false` and `nil` are false. Everything else is true.
- Arithmetic operators require numbers.
- The `+` operator works with two numbers or two strings.
- Different types are not automatically converted.
- Invalid operations display runtime errors.

## Running

Interactive mode:

`python src/breezy.py`

File mode:

`python src/breezy.py test/lab4/arithmetic.bzy`

## Tests

| Test | Input | Expected Output |
|---|---|---|
| Arithmetic | `10 + 5 * 2` | `20.0` |
| Strings | `"Hello" + " Breezy"` | `Hello Breezy` |
| Comparison | `(10 > 5) == (3 < 8)` | `true` |
| Mixed types | `10 + "Hello"` | Runtime error |
| Truthiness | `!0` | `false` |
| Unary minus | `-(10 + 5)` | `-15.0` |
| Invalid unary | `-true` | Runtime error |
| Division by zero | `10 / 0` | Runtime error |

## Post-Order Traversal Example

Expression: `10 + 5 * 2`

```text
       +
      / \
    10   *
        / \
       5   2
```

The evaluator first calculates `5 * 2 = 10`. Then it adds `10 + 10` to get `20`.

## Error Handling

Breezy checks operand types before evaluating operations. If an operation is invalid, it displays a runtime error instead of crashing. Interactive mode continues after an error.

## Known Limitations

Breezy currently evaluates one expression at a time. It does not support variables, statements, or functions yet.