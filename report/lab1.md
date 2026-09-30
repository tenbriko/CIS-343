# Lab 1: Scanning

## Language Design

My language is called **Breezy** and is based on Lox.

Changes from Lox:
- `let` instead of `var`
- `function` instead of `fun`
- `show` instead of `print`

Keywords: `and`, `else`, `false`, `for`, `function`, `if`, `or`, `show`, `return`, `true`, `let`, `while`

Operators: `(` `)` `{` `}` `,` `.` `;` `+` `-` `*` `/` `!` `!=` `=` `==` `<` `<=` `>` `>=`

Comments use `//`. Spaces and tabs are ignored.

## Regex

Number: `[0-9]+(\.[0-9]+)?`

String: `"[^"]*"`

Identifier: `[A-Za-z_][A-Za-z0-9_]*`

## Running

Interactive:

`python src/breezy.py`

File:

`python src/breezy.py test/lab1/basic.bzy`

// --- start AI code ---

// -- I had AI give me inputs to test each of my methods. Then I ran each input to confirmed that each one did pass the requirements for each method I had. -- 

## Tests

### Basic
Purpose: Test a basic Breezy program.  
Input: Variables, strings, numbers, `show`, and `if`.  
Expected: Correct tokens.  
Actual: Correct tokens.  
Result: **PASS**

### Operators
Purpose: Test operators and punctuation.  
Input: `(){} , . ; + - * / ! != = == < <= > >=`  
Expected: Correct operator tokens.  
Actual: Correct operator tokens.  
Result: **PASS**

### Keywords
Purpose: Test all keywords.  
Input: `and else false for function if or show return true let while`  
Expected: Correct keyword tokens.  
Actual: Correct keyword tokens.  
Result: **PASS**

### Literals
Purpose: Test numbers, strings, and identifiers.  
Input: `123`, `45.67`, `"Hello"`, `name`, `player1`, `my_variable`  
Expected: Correct literal and identifier tokens.  
Actual: Correct tokens.  
Result: **PASS**

### Errors
Purpose: Test scanner errors.

Input:
```text
@
$
"Unterminated string
```

Expected: Three errors with correct line numbers.

Actual:
```text
[line 1] Error: Unexpected character '@'.
[line 2] Error: Unexpected character '$'.
[line 3] Error: Unterminated string.
```

Result: **PASS**

### Interactive Mode
Purpose: Test recovery after an error.  
Input: Invalid input followed by valid input.  
Expected: Report the error and continue running.  
Actual: Breezy continued running.  
Result: **PASS**

// --- end AI code ---

## Known Limitations

Breezy only scans code right now. It does not parse or execute code. It also does not support block comments or string escape characters.

