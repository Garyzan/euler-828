# Project Euler Problem 828 Equation Solver
![docs](https://github.com/garyzan/euler-828/actions/workflows/docs.yml/badge.svg)
![test coverage](https://github.com/garyzan/euler-828/actions/workflows/tests.yml/badge.svg)
[![release](https://img.shields.io/badge/release-v0.1.0-blue.svg)](https://img.shields.io/badge/release-v0.1.0-blue.svg)
[![license](https://img.shields.io/badge/license-GPLv3-green.svg)](https://img.shields.io/badge/license-GPLv3-green.svg)

This project provides an algorithm that uses a set of given numbers and tries to construct an equation which evaluates to a specified target number. It will try to find the equation(s), in which the sum of the operands is minimal for the given problem. 

## Installation

Install via pip:

```
pip install euler828
```

## Usage

You can declare a problem by using the `Problem` class and providing it with a target number as well as a list of operands from which the equation should be constructed:

```python
from euler828.problem import Problem

problem = Problem(target = 10, operands = [1,2,5])
```

You can then solve the problem by calling `solve()`:

```python
from euler828 import solve
from euler828.problem import Problem


problem = Problem(target = 10, operands = [1,2,5])
score, expressions = solve(problem = problem)
```

The `solve()` function returns the lowest possible score as well as all expressions that yield the correct number with that score. If the problem is unsolvable, it will return 0 and an empty list.

You can also provide the `solve()` function with the target and operands directly:

```python
from euler828 import solve

score, expressions = solve(target = 10, operands = [1,2,5])
```

## Testing

TBD