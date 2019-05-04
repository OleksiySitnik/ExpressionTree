import sys

from .expressionsystem import ExpressionSystem

if __name__ == '__main__':
    expressions = ExpressionSystem(sys.argv[1])
    expressions.solution()
