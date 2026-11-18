from expr import Binary, Unary, Grouping, Literal, Variable, Assign
from stmt import Expression, Show, Var, Block
from environment import Environment


class Evaluator:
    def __init__(self):
        self.environment = Environment()

    def execute(self, stmt):
        if isinstance(stmt, Expression):
            self.evaluate(stmt.expression)

        elif isinstance(stmt, Show):
            value = self.evaluate(stmt.expression)
            print(self.stringify(value))
        
        elif isinstance(stmt, Var):
            value = None

            if stmt.initializer is not None:
                value = self.evaluate(stmt.initializer)

            if stmt.name.lexeme in self.environment.values:
                self.error(stmt.name, f"Variable '{stmt.name.lexeme}' is already declared in this scope.")

            self.environment.define(stmt.name.lexeme, value)

        elif isinstance(stmt, Block):
            self.execute_block(stmt.statements, Environment(self.environment))

    def execute_block(self, statements, environment):
        previous = self.environment

        try:
            self.environment = environment

            for statement in statements:
                self.execute(statement)

        finally:
            self.environment = previous
    
    def stringify(self, value):
        if value is None:
            return "nil"

        if value is True:
            return "true"

        if value is False:
            return "false"

        return str(value)

    def evaluate(self, expr):
        if isinstance(expr, Literal):
            return expr.value

        if isinstance(expr, Grouping):
            return self.evaluate(expr.expression)
        
        if isinstance(expr, Variable):
            return self.environment.get(expr.name)

        if isinstance(expr, Assign):
            value = self.evaluate(expr.value)
            self.environment.assign(expr.name, value)
            return value

        if isinstance(expr, Unary):
            right = self.evaluate(expr.right)
            operator = expr.operator.lexeme

        if operator == "!":
            return not self.is_truthy(right)

        if operator == "-":
            self.check_number(right, expr.operator)
            return -right

        if isinstance(expr, Binary):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)
            operator = expr.operator.lexeme

            left = self.to_number(left)
            right = self.to_number(right)

            if operator == "+":
                if type(left) == float and type(right) == float:
                    return left + right

                if type(left) == str and type(right) == str:
                    return left + right

                self.error(expr.operator, "Operands must be two numbers or two strings.")

            if operator in ("-", "*", "/", ">", ">=", "<", "<="):
                self.check_numbers(left, right, expr.operator)

                if operator == "-":
                    return left - right

                if operator == "*":
                    return left * right

                if operator == "/":
                    if right == 0:
                        self.error(expr.operator, "Cannot divide by zero.")
                    return left / right

                if operator == ">":
                    return left > right

                if operator == ">=":
                    return left >= right

                if operator == "<":
                    return left < right

                if operator == "<=":
                    return left <= right

            if operator == "==":
                return left == right

            if operator == "!=":
                return left != right

        raise RuntimeError("Unknown expression.")

    def is_truthy(self, value):
        if value is None or value is False:
            return False
        return True

    def to_number(self, value):
        if value is True:
            return 1.0

        if value is False:
            return 0.0

        return value

    def check_number(self, value, token):
        if type(value) != float:
            self.error(token, "Operand must be a number.")

    def check_numbers(self, left, right, token):
        if type(left) != float or type(right) != float:
            self.error(token, "Operands must be numbers.")

    def error(self, token, message):
        raise RuntimeError(f"[line {token.line}] Runtime Error: {message}")
