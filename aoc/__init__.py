from contextlib import redirect_stdout
import importlib
import os
import pathlib

from aoc import config


def plugin(year, day, data):
    yn = config.year_folder.format(year=year)
    dn = pathlib.Path(config.solution_filename.format(day=day)).stem

    with open(os.devnull, "w") as devnull:
        with redirect_stdout(devnull):
            solution_module = importlib.import_module(f"aoc.{yn}.{dn}")
            solution = solution_module.solve(data)
        #

    return solution

