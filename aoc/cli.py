import argparse
import datetime
import pathlib
from termcolor import cprint

from aoc import config
from aoc.template_tools import make_solution_draft
from aoc.tokens import quicktest

_now = datetime.datetime.now()
tis_the_season = _now.month == 12

year_min = 2015
year_max = _now.year if tis_the_season else _now.year - 1
year_default = _now.year if tis_the_season else None

day_min = 1
day_max = 25
day_default = _now.day if tis_the_season and (day_min <= _now.day <= day_max) else None


def prompt_for_value(prompt: str, lower: int, upper: int, default: int=None) -> int:
    if default is not None:
        prompt += f" (press enter to use {default})"
    prompt += ": "
    
    while True:
        s = input(prompt)
        if not s and default is not None:
            cprint(f"Defaulting to {default}", color='green')
            return default
        try:
            x = int(s)
            if lower <= x <= upper:
                cprint(f"Got input: {x}", color='green')
                return x
            else:
                raise ValueError
        except ValueError:
            cprint(f"Invalid input - enter a number between {lower} and {upper}", color='red')
        #
    #   


def initialize():
    parser = argparse.ArgumentParser(description="Initialize solution for a new day")
    parser.add_argument(
        "--day",
        "-d",
        type=int,
        default=None,
        help=f"{day_min}-{day_max} (default: %(default)s)",
    )
    parser.add_argument(
        "--year",
        "-y",
        type=int,
        default=None,
        help=f"{year_min}-{year_max} (default: %(default)s)",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="create the template file even if source already exists",
    )

    args = parser.parse_args()
    n_none = sum(arg is None for arg in (args.day, args.year))
    if n_none == 1:
        raise ValueError(f"Either specify both day and year, or neither!")

    day = args.day
    year = args.year
    
    if day is None:
        day = prompt_for_value("Enter day", lower=day_min, upper=day_max, default=day_default)
    if year is None:
        year = prompt_for_value("Enter year", lower=year_min, upper=year_max, default=year_default)
    
    looks_good = quicktest()
    if looks_good:
        cprint(f"Got session token.", color='green')
    else:
        cprint(f"Could not locate session token - sign into adventofcode.com in a browser and try again.", color='red')

    print(f"Initializing solution for year {year}, day {day}...")

    solution_draft = make_solution_draft(year=year, day=day)
    
    print(solution_draft)
    path = config.make_path(year=year, day=day)
    
    path.parent.mkdir(parents=True, exist_ok=True)

    if pathlib.Path(path).exists() and not args.force:
        print(f"Solution file {path} already exist and --force is not set. Aborting.")
        return

    with open(path, "w") as f:
        f.write(solution_draft)
    #


if __name__ == '__main__':
    initialize()