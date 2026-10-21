
from expr import Binary, Unary, Grouping, Literal


class Evaluator:
    def evaluate(self, expr):
        if isinstance(expr, Literal):
            return expr.value

        if isinstance(expr, Grouping):
            return self.evaluate(expr.expression)

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
                return type(left) == type(right) and left == right

            if operator == "!=":
                return not (type(left) == type(right) and left == right)

        raise RuntimeError("Unknown expression.")

    def is_truthy(self, value):
        if value is None or value is False:
            return False
        return True

    def check_number(self, value, token):
        if type(value) != float:
            self.error(token, "Operand must be a number.")

    def check_numbers(self, left, right, token):
        if type(left) != float or type(right) != float:
            self.error(token, "Operands must be numbers.")

    def error(self, token, message):
        raise RuntimeError(f"[line {token.line}] Runtime Error: {message}")
