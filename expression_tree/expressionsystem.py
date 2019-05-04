from expression_tree.errors import ExpressionSyntaxError, VariableNameError, UndefinedVariableError
from expression_tree.expression_ import Expression
from expression_tree.tree import BinaryTree, Root


class ExpressionSystem:

    def __init__(self, file):
        self._file = file
        self._expressions = []
        # self.expressions = [Expression(line[:-1]) for line in open(file)]

    @property
    def expressions(self):
        if self._expressions:
            return self._expressions

        with open(self._file) as f:
            for line in f:
                if line[:-1]:
                    expression = line[:-1] if line[-1] == "\n" else line
                    self._expressions.append(Expression(expression))

        return self._expressions

    def build_full_tree(self):
        root = Root()

        for i, expression in enumerate(self.expressions):

            if str(expression).startswith(">>"):

                root.kids.append(BinaryTree(">>"))
                root[-1].left = expression.binary_tree()

            elif ~str(expression).find("="):

                left_part, right_part = str(expression).split("=")

                root.kids.append(BinaryTree("="))
                root[-1].left = BinaryTree(left_part)
                root[-1].right = Expression(right_part).binary_tree()

            else:
                raise ExpressionSyntaxError('Syntax error in "{}", line {} in file "{}"'
                                            .format(expression, i + 1, self._file))

        return root

    def solution(self):
        """Finds the values of all variables and
        print values of expressions that begin with ">>"

        Dictionary variables using for saving values of variables
        and for using this values in following operations and expressions
        """
        variables = {}

        res_tree = self.build_full_tree()

        for i in range(len(res_tree.kids)):

            try:
                res_tree[i].fill_temp_value(variables)

            except AttributeError:
                raise ExpressionSyntaxError('Syntax error in "{}", line {} in file "{}"'
                                            .format(self._expressions[i], i + 1, self._file))

            except (TypeError, IndexError):
                raise VariableNameError('Invalid variable name in "{}", line {} in file "{}"'
                                        .format(self._expressions[i], i + 1, self._file))

            if res_tree[i].value == ">>":
                expression = str(self.expressions[i])[2:]
                result = res_tree[i].left.temp_value

                if result is None:
                    raise UndefinedVariableError('Undefined variable name in "{}", line {} in file {}'
                                        .format(self._expressions[i], i + 1, self._file))

                print("{} = {}".format(expression.strip(), round(result, 3)))
                variables[expression] = round(result, 3)

        return variables


if __name__ == "__main__":
    expr = ExpressionSystem("tests/fixtures/test_6.txt")
    print(expr.solution())

    expr_1 = ExpressionSystem("tests/fixtures/test_2.txt")
    expr_1.solution()
