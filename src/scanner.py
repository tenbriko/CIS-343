from token_type import TokenType
from token import Token


class Scanner:
    keywords = {
        "and": TokenType.AND,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "function": TokenType.FUNCTION,
        "if": TokenType.IF,
        "or": TokenType.OR,
        "show": TokenType.SHOW,
        "return": TokenType.RETURN,
        "true": TokenType.TRUE,
        "let": TokenType.LET,
        "while": TokenType.WHILE,
    }
    def __init__(self, source):
        self.source = source
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()

        if c == "(":
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ")":
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == "{":
            self.add_token(TokenType.LEFT_BRACE)
        elif c == "}":
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == ",":
            self.add_token(TokenType.COMMA)
        elif c == ".":
            self.add_token(TokenType.DOT)
        elif c == "-":
            self.add_token(TokenType.MINUS)
        elif c == "+":
            self.add_token(TokenType.PLUS)
        elif c == ";":
            self.add_token(TokenType.SEMICOLON)
        elif c == "*":
            self.add_token(TokenType.STAR)
        elif c == "!":
            if self.match("="):
                self.add_token(TokenType.BANG_EQUAL)
            else:
                self.add_token(TokenType.BANG)
        elif c == "=":
            if self.match("="):
                self.add_token(TokenType.EQUAL_EQUAL)
            else:
                self.add_token(TokenType.EQUAL)
        elif c == "<":
            if self.match("="):
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)
        elif c == ">":
            if self.match("="):
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)
        elif c == "/":
            if self.match("/"):
                # Ignore everything until the end of the line
                while self.peek() != "\n" and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)

        # Ignore spaces and tabs
        elif c == " " or c == "\r" or c == "\t":
            pass

        # Keep track of line numbers
        elif c == "\n":
            self.line += 1
        elif c == '"':
            self.string()
        elif self.is_digit(c):
            self.number()
        elif self.is_alpha(c):
            self.identifier()
        else:
            print(f"[line {self.line}] Error: Unexpected character '{c}'.")

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        c = self.source[self.current]
        self.current += 1
        return c

    def match(self, expected):
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    def peek(self):
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def add_token(self, token_type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(
            Token(token_type, text, literal, self.line)
        )

    def is_digit(self, c):
        return c >= "0" and c <= "9"

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        # Look for a decimal
        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()
        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def string(self):
        starting_line = self.line
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()
        if self.is_at_end():
            print(f"[line {starting_line}] Error: Unterminated string.")
            return

        # Consume the closing "
        self.advance()

        # Remove the surrounding quotation marks
        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)

    def is_alpha(self, c):
        return (
            ("a" <= c <= "z")
            or ("A" <= c <= "Z")
            or c == "_"
        )

    def is_alpha_numeric(self, c):
        return self.is_alpha(c) or self.is_digit(c)

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        text = self.source[self.start:self.current]
        token_type = self.keywords.get(
            text,
            TokenType.IDENTIFIER
        )
        self.add_token(token_type)