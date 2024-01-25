import os
from problem import Problem

class Reader:
    def __init__(self) -> None:
        pass

    def parse_problem(self, problem: str) -> Problem:
        target, ops = problem.split(":")
        target = int(target)
        ops = [int(k) for k in ops.split(",")]
        return Problem(target, ops)

    def read_file(self, path : os.PathLike | str) -> list[Problem]:
        with open(path, "r") as f:
            lines = f.readlines()
            problems : list[Problem] = []
            for line in lines:
                problems.append(self.parse_problem(line.rstrip()))
        return problems
