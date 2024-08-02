# Development notes

## Badges

[![testing](https://github.com/jspaaks/copier-template-for-c-projects/actions/workflows/testing.yml/badge.svg)](https://github.com/jspaaks/copier-template-for-c-projects/actions/workflows/testing.yml)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/jspaaks/copier-template-for-c-projects/0.1.0)](https://github.com/jspaaks/copier-template-for-c-projects/compare/0.1.0...HEAD)

## Testing

Running the tests requires Python libraries specified in `pyproject.toml`,
as well as `cmake` and `make` binaries, and `Criterion` testing library.

Directory `fuzzy` contains fuzzy tests. Run with:

```shell
python3 -m venv venv
source venv/bin/activate
pip install .[testing]
# Run pytest with default settings from pyproject.toml
NFUZZY=50 pytest
# Run pytest verbosely and for a specific test (test_clang_format_generation),
# report stdout in case of failure
NFUZZY=10 pytest fuzzy/test_template.py::test_clang_format_generation -ra --verbose
```

By changing the value of `NFUZZY`, you can run more or fewer fuzzy tests.

Testing includes running the generated tests on the generated content. Since this requires additional dependencies
(e.g. Criterion and its dependencies, CMake, some build system like make, etc), it's sometimes convenient to skip
those tests. To that end, they have been marked with a Pytest marker 'inception' which should be used as follows in
order to skip those tests:

```
NFUZZY=10 pytest -m 'not inception'
```

For an overview of all pytest markers, see [pyproject.toml](/pyproject.toml).

On Windows and Mac you may need to fiddle with various path-related environment variables, see the testing workflow [`.github/workflows/testing.yml`](/.github/workflows/testing.yml).

## Other stuff

### checks

1. tests pass
2. codeblocks project files opens
3. file exists for every file in codeblocks filetree
4. codeblocks project builds
5. codeblocks project runs

### results 

|      |        |               | checked    | state   |
| ---  | ---    | ---           | ---        | ---     |
| both | flat   | with-external | 2024-07-22 | ok      |
| both | flat   | wo-external   | 2024-07-22 | ok      |
| both | nested | with-external | 2024-07-22 | ok      |
| both | nested | wo-external   | 2024-07-22 | ok      |
| exe  | flat   | with-external | 2024-07-22 | ok      |
| exe  | flat   | wo-external   | 2024-07-22 | ok      |
| exe  | nested | with-external | 2024-07-22 | ok      |
| exe  | nested | wo-external   | 2024-07-22 | ok      |
| lib  | flat   | with-external | 2024-07-22 | ok      |
| lib  | flat   | wo-external   | 2024-07-22 | ok      |
| lib  | nested | with-external | 2024-07-22 | ok      |
| lib  | nested | wo-external   | 2024-07-22 | ok      |
