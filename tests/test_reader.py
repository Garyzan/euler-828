import pytest
from euler828 import reader

targets = [211, 321, 197]
all_operands = [[2,3,4,6,7,25],
                [3,7,8,10,10,100],
                [1,3,6,9,50,75]]

def test_parse():
    problem_str = "907:1,2,7,7,25,100"
    result = reader.parse_problem(problem_str)
    assert result.target == 907
    assert all([a == b for a, b in zip(result.operands, [1,2,7,7,25,100])])

def test_read_file(tmp_path):
    f = tmp_path / "example_data.txt"
    f.write_text("211:2,3,4,6,7,25\n321:3,7,8,10,10,100\n197:1,3,6,9,50,75")
    problems = reader.read_file(f)
    assert len(problems) == 3
    for target, operands, problem in zip(targets, all_operands, problems):
        assert problem.target == target
        assert all([a == b for a, b in zip(problem.operands, operands)])