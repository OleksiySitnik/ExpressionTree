from collections import deque

from expression_tree.check_type_and_priority import is_operator, get_priority
from expression_tree.tree import BinaryTree


class Expression:
    """
    >>> e = Expression("1-4.5^a/554")
    >>> e._reverse_polish_notation()
    deque(['1', '4.5', 'a', '^', '554', '/', '-'])

    >>> e.binary_tree()
        1
    -
                4.5
            ^
                a
        /
            554

    """

    def __init__(self, string_expression):
        self._expression = string_expression

    def __str__(self):
        return self._expression

    def _reverse_polish_notation(self):
        """Convert expression to reverse polish notation.

        >>> Expression("1-4.5^a/554")._reverse_polish_notation()
        deque(['1', '4.5', 'a', '^', '554', '/', '-'])

        >>> Expression("a1-1.4**(14+b)/18")._reverse_polish_notation()
        deque(['a1', '1.4', '*', '14', 'b', '+', '*', '18', '/', '-'])

        """
        output_values = deque()
        stack_operators = deque()
        temp_str = ""

        for element in self._expression:
            if element.isalnum() or element == ".":
                temp_str += element
                continue

            if temp_str:
                output_values.append(temp_str)
            temp_str = ""

            if element == "(":
                stack_operators.append(element)

            elif element == ")":
                while len(stack_operators) and stack_operators[-1] != "(":
                    output_values.append(stack_operators.pop())
                stack_operators.pop()

            elif is_operator(element):
                while (len(stack_operators) and
                       get_priority(stack_operators[-1]) >= get_priority(element)):
                    output_values.append(stack_operators.pop())

                stack_operators.append(element)

        if temp_str:
            output_values.append(temp_str)

        while len(stack_operators) != 0:
            output_values.append(stack_operators.pop())

        return output_values

    def binary_tree(self):
        """Build binary tree with expression using reverse polish notation

        >>> Expression("(543+1.1)/(19-4)").binary_tree()
                543
            +
                1.1
        /
                19
            -
                4

        """
        elements_in_polish_not = self._reverse_polish_notation()
        root = BinaryTree(elements_in_polish_not.pop())

        for element in reversed(elements_in_polish_not):

            if is_operator(element):

                if not root.left:
                    root.left = BinaryTree(element)
                    root = root.left

                else:
                    while root.right:
                        root = root.parent
                    root.right = BinaryTree(element)
                    root = root.right

            else:
                if not root.left:
                    root.left = BinaryTree(element)

                elif not root.right:
                    root.right = BinaryTree(element)

                else:
                    while root.right:
                        root = root.parent
                    root.right = BinaryTree(element)

        while root.parent is not None:
            root = root.parent
        return root


if __name__ == "__main__":
    import doctest
    doctest.testmod()
