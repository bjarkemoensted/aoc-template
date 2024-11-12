# Advent of Code quickstart template

## TL;DR
* Set up and activate environment with poetry
* Sign into [adventofcode.com](adventofcode.com) in a browser (to make sure a session token is available)
* Run `aoc-init` to make a solution draft file

## Setup
Set up and activate environment with poetry:
```bash
poetry install
poetry shell
```

Sign into [adventofcode.com](adventofcode.com) to make sure a session token is stored in your browser.

## Set up a new solution draft
From the poetry shell, type `aoc-init` to create a draft for a solution. 
The script will prompt for which the day/year to set up a solution draft for.
The template for the draft is the `solution_template.py` jinja template, which can be customized. The file name and folder structure for new solutions is defined in `config.py`.

This project uses functionality from [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data) to obtain session tokens from the browser cache. In case of issues with extracting the token, check the readme there. Alternatively, signing in with a different browser might work (Firefox seems to always work well).