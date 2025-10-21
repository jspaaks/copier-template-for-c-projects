# Development notes

## Badges

[![testing](https://github.com/jspaaks/copier-template-for-c-projects/actions/workflows/testing.yml/badge.svg)](https://github.com/jspaaks/copier-template-for-c-projects/actions/workflows/testing.yml)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/jspaaks/copier-template-for-c-projects/0.1.0)](https://github.com/jspaaks/copier-template-for-c-projects/compare/0.1.0...HEAD)

## Testing

Running the tests requires Python libraries specified in `pyproject.toml`.

Directory `fuzzy` contains fuzzy tests. Each fuzzy test is a random combination of parameter values for the parameters
from [`copier.yml`](copier.yml). Each parameterization runs on a dedicated temporary test directory. Run with:

```shell
python3 -m venv venv
source venv/bin/activate
pip install .[testing]
# Run pytest with default settings from pyproject.toml
NFUZZY=50 pytest
# Run pytest verbosely and for a specific test (here: test_clang_format_generation),
# report stdout in case of failure
NFUZZY=10 pytest fuzzy/test_template.py::test_clang_format_generation -ra --verbose
```

Change the value of `NFUZZY` to run more or fewer fuzzy tests.

By default, testing includes running the generated tests on the generated content. Since this requires additional
dependencies (e.g. Criterion and its dependencies, CMake, some build system like `make`, a C compiler, etc), it's sometimes convenient to
skip those tests. To that end, they have been marked with a PyTest marker `inception` which should be used as follows in
order to skip those tests:

```
NFUZZY=10 pytest -m 'not inception'
```

For an overview of all pytest markers, see [`pyproject.toml`](pyproject.toml) or run:

```console
$ pytest --markers
```

On Windows and Mac you may need to fiddle with various path-related environment variables, see the testing
workflow [`.github/workflows/testing.yml`](.github/workflows/testing.yml).

# Live editing / rendering of Jinja templates

https://j2live.ttl255.com/
