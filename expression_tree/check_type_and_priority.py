operators = ['+', '-', '/', '*', '^', '=']
braces = ['(', ')']


def is_operator_or_brace(char):
    return (char in operators) or (char in braces)


def is_operator(char):
    return char in operators


def get_priority(c):
    priorities = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return priorities.get(c, 0)

if __name__ == "__main__":
    print(__path__)