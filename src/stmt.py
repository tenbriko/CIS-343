
class Expression:
    def __init__(self, expression):
        self.expression = expression


class Show:
    def __init__(self, expression):
        self.expression = expression

class Var:
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer


class Block:
    def __init__(self, statements):
        self.statements = statements