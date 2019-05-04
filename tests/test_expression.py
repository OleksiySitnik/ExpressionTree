import pytest

from expression_tree.expression_ import Expression


@pytest.mark.parametrize("expression, expected_pn", [

])
def test_polish_notation(expression, expected_pn):
    assert Expression(expression)._reverse_polish_notation() == expected_pn
