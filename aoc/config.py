import pathlib

_here = pathlib.Path(__file__).resolve().parent
root_dir = _here.parents[1]

solution_template_path = _here / "solution_template.py"

solution_filename = "solution{day:02d}.py"
year_folder       = "aoc_{year:04d}"


def make_path(year: int, day: int) -> pathlib.Path:
    res = pathlib.Path(_here) / year_folder.format(year=year) / solution_filename.format(day=day)
    return res


if __name__ == '__main__':
    pass
