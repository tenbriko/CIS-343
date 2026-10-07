from expr import Binary, Grouping, Literal, Unary


class AstPrinter:
    def print(self, expr):
        return self.print_expr(expr)

    def print_expr(self, expr):
        if isinstance(expr, Binary):
            return self.parenthesize(
                expr.operator.lexeme,
                expr.left,
                expr.right
            )

        if isinstance(expr, Grouping):
            return self.parenthesize(
                "group",
                expr.expression
            )

        if isinstance(expr, Literal):
            if expr.value is None:
                return "nil"
            if expr.value is True:
                return "true"
            if expr.value is False:
                return "false"
            return str(expr.value)

        if isinstance(expr, Unary):
            return self.parenthesize(
                expr.operator.lexeme,
                expr.right
            )

    def parenthesize(self, name, *expressions):
        result = "(" + name

        for expression in expressions:
            result += " " + self.print_expr(expression)

        result += ")"
        return result