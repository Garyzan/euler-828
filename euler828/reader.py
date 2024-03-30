import os

from .problem import Problem

def parse_problem(problem: str) -> Problem:
    """Parses a string yontaining a problem in the format
    `[target]:[operand],[operand],...`.
    
    Parameters
    ----------
    problem : str
        Text representation of the problem.
    
    Returns
    -------
    Problem
        Problem object containing the problem.
    """
    target, operands = problem.split(":")
    target = int(target)
    operands = [int(k) for k in operands.split(",")]
    return Problem(target, operands)

def read_file(path : os.PathLike | str) -> list[Problem]:
    """Parses a file in which every line contains a problem in the format
    `[target]:[operand],[operand],...`.

    Parameters
    ----------
    path : path-like object or str
        File Path to file to be read.
    
    Returns
    -------
    list of Problems
        List of all problems contained in the file.
    """
    with open(path, "r") as f:
        lines = f.readlines()
        problems : list[Problem] = []
        for line in lines:
            problems.append(parse_problem(line.rstrip()))
    return problems
