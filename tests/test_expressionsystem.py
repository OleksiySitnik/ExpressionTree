import pytest

from expression_tree.expressionsystem import ExpressionSystem

expected_results = [
    {},
    {'c': 10, 'c21d': 480, 'r1': 160},
    {'a': 20, 'b': 160},
    {'y': 19.1, 'x': 169.0, '(x+y)*5.1': 959.31},
    {' b': 1, 'a': 9, 'b': 1},
    {'a1': 6.0, 'a2': 12.0, 'a3': 4.0},
    {'m': -275706.0, 'abc': 2703.0, '(abc/4)^2': 456638.062, 'q': 7803.0, '2-abc/q': 0.961}
]

expected_stdout_results = [
    ''
    ,
    'r1 = 160.0\n'
    'c21d = 480.0\n'
    ,
    'a = -4.0\n'
    'a = 20.0\n'
    'b = 160.0\n'
    ,
    '(x+y)*5.1 = 959.31\n'
    ,
    'b = -7.0\n'
    'b = 1.0\n'
    ,
    ''
    ,
    'q = 2601.0\n'
    'abc = 2703.0\n'
    '2-abc/q = 0.961\n'
    '(abc/4)^2 = 456638.062\n'
    'q = 7803.0\n'
    'abc = 2703.0\n'
]


@pytest.mark.parametrize("file, expected", [
    ("tests/fixtures/test_{}.txt".format(i), expected_results[i - 1]) for i in range(1, 8)
])
def test_solution(file, expected):
    assert ExpressionSystem(file).solution() == expected


@pytest.mark.parametrize("file, expected_stdout", [
    ("tests/fixtures/test_{}.txt".format(i), expected_stdout_results[i - 1]) for i in range(1, 8)
])
def test_solution_stdout(file, expected_stdout, capsys):
    ExpressionSystem(file).solution()
    captured = capsys.readouterr()

    assert captured.out == expected_stdout
