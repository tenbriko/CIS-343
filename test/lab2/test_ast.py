import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from expr import Binary, Grouping, Literal, Unary
from ast_printer import AstPrinter
from token import Token
from token_type import TokenType


expression = Binary(
    Unary(
        Token(TokenType.MINUS, "-", None, 1),
        Literal(123)
    ),
    Token(TokenType.STAR, "*", None, 1),
    Grouping(
        Literal(45.67)
    )
)

expression2 = Binary(
    Literal(10),
    Token(TokenType.PLUS, "+", None, 1),
    Binary(
        Literal(5),
        Token(TokenType.SLASH, "/", None, 1),
        Literal(2)
    )
)

expression3 = Binary(
    Unary(
        Token(TokenType.BANG, "!", None, 1),
        Literal(False)
    ),
    Token(TokenType.EQUAL_EQUAL, "==", None, 1),
    Grouping(
        Literal(True)
    )
)

expression4 = Binary(
    Binary(
        Literal(10),
        Token(TokenType.GREATER_EQUAL, ">=", None, 1),
        Literal(5)
    ),
    Token(TokenType.BANG_EQUAL, "!=", None, 1),
    Binary(
        Literal(3),
        Token(TokenType.LESS, "<", None, 1),
        Literal(8)
    )
)

expression5 = Binary(
    Binary(
        Literal(10),
        Token(TokenType.MINUS, "-", None, 1),
        Literal(4)
    ),
    Token(TokenType.GREATER, ">", None, 1),
    Binary(
        Literal(3),
        Token(TokenType.LESS_EQUAL, "<=", None, 1),
        Literal(None)
    )
)

printer = AstPrinter()

print(printer.print(expression))
print(printer.print(expression2))
print(printer.print(expression3))
print(printer.print(expression4))
print(printer.print(expression5))

expression6 = Literal("Hello Breezy")

print(printer.print(expression6))