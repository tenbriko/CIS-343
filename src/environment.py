class Environment:
    def __init__(self, enclosing=None):
        self.values = {}
        self.enclosing = enclosing

    def define(self, name, value):
        if name in self.values:
            raise RuntimeError(f"Variable '{name}' is already declared in this scope.")

        self.values[name] = value

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise RuntimeError(
            f"[line {name.line}] Runtime Error: Undefined variable '{name.lexeme}'."
        )

    def assign(self, name, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return

        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return

        raise RuntimeError(
            f"[line {name.line}] Runtime Error: Undefined variable '{name.lexeme}'."
        )
