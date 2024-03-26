import os

from problem import Problem

def parse_problem(problem: str) -> Problem:
    target, operands = problem.split(":")
    target = int(target)
    operands = [int(k) for k in operands.split(",")]
    return Problem(target, operands)

def read_file(path : os.PathLike | str) -> list[Problem]:
    with open(path, "r") as f:
        lines = f.readlines()
        problems : list[Problem] = []
        for line in lines:
            problems.append(parse_problem(line.rstrip()))
    return problems
