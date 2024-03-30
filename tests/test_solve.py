import pytest

import euler828.solver as solver

problem_1 = [211, [2,3,4,6,7,25]]
sol_1 = [40, 2]

problem_2 = [1000000, [1, 3, 5, 7, 9, 11]]
sol_2 = [0, 0]


@pytest.mark.parametrize("problem, expected_solution", [(problem_1, sol_1), (problem_2, sol_2)])
def test_solve(problem, expected_solution):
    score, expressions = solver.solve(target=problem[0], operands=problem[1])

    assert score == expected_solution[0]
    assert len(expressions) == expected_solution[1]
    assert all([expression.evaluate() == problem[0] for expression in expressions])
    assert all([expression.score == expected_solution[0] for expression in expressions])