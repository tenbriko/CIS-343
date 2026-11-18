# Lab 5: Variables and Scope

## Overview
In this lab, I added variables and block scopes to my Breezy interpreter. Variables can now be declared, accessed, and updated.

## Implementation
- Updated `expr.py` and `stmt.py` with new classes.
- Updated `parser.py` to recognize variables, assignments, and blocks.
- Created `environment.py` to store variables and manage scopes.
- Updated `evaluator.py` to handle variables and blocks.
- Updated `breezy.py` to remember variables between commands.

## Design Choices
- Using a variable before declaring it gives an error.
- Variables without a starting value are set to `nil`.
- Declaring the same variable twice in one scope gives an error.
- Variables can have the same name in different scopes.

## Testing
I tested variable declarations, assignments, nested scopes, and error handling.

The nested scope test produced:

```text
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c
```

I also tested undefined variables, invalid assignments, and missing or extra braces. All tests passed.

## Conclusion
I successfully added variables and block scopes to Breezy. The interpreter can now store and update variables while keeping block scopes separate.