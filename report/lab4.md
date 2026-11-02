# Lab 4: Statements

## Overview

For this lab, I added expression statements and show statements to my Breezy programming language. I also added panic-mode error recovery so the parser can continue after finding syntax errors.

## Design

I created `stmt.py` to represent expression statements and show statements. I updated `parser.py` to recognize multiple statements and added `synchronize()` for error recovery.

I also updated `evaluator.py` to execute statements and `breezy.py` to run multiple statements from a file.

Breezy uses `show` instead of `print`.

## Running

Interactive mode:

`py src/breezy.py`

File mode:

`py src/breezy.py test/lab4/statements.bzy`

## Test 1: Statements

Input:

```text
4 + 2;
show "one";
show true;
show 1 + 2;
show nil;
```

Output:

```text
one
true
3.0
nil
```

The expression statement `4 + 2;` is evaluated without printing a result. The show statements display their values.

## Test 2: Panic-Mode Error Recovery

Input:

```text
"one"
true;
show 2 +
show "Recovered!";
```

Output:

```text
[line 2] Error at 'true': Expected ';' after expression.
[line 4] Error at 'show': Expected expression.
Recovered!
```

The parser reports syntax errors and continues parsing. The final valid show statement still executes.

## Error Handling

I added a `synchronize()` function to the parser. When a syntax error occurs, the parser skips tokens until it finds a statement boundary or another statement keyword. This allows Breezy to continue instead of stopping completely.

## Known Limitations

Breezy currently supports expression statements and show statements. Variables, loops, and functions are not implemented yet.
