# {{ cookiecutter.project_slug }}

{% if cookiecutter.add_cmake -%}

## CMake

The project has been initialized with a [CMakeLists.txt](CMakeLists.txt)-based
configuration for building with CMake:

```shell
# change into the build directory
cd {{ cookiecutter.build_directory }}/cmake

# generate the build files
cmake ../..

# build the project
make

# install the project to <repo>/build/dist
make install
{% if cookiecutter.produces in ["exe", "both"] %}
# run the program to see if it works
./dist/bin/{{ cookiecutter.project_slug }}
```

Should output something like:

```text
-- test compile definitions
   DEBUG compile definition has been defined.

-- test wether math library was linked
   sqrt(144) = 12.000000

-- test c2x / c23 features
   0 1 2 3 4

-- test own library
   divide(2, 3) = 0
   multiply(2, 3) = 6

{% if cookiecutter.external_directory != "My project doesn't have external dependencies" -%}
-- test external library
   add(2, 3) = 5
   subtract(2, 3) = -1
{% endif -%}
{% endif -%}
```

{% endif -%}

{% if cookiecutter.add_codeblocks -%}

## Code::Blocks

Use [Code::Blocks IDE](https://www.codeblocks.org/) to open [.codeblocks/project.cbp](.codeblocks/project.cbp). 

{% endif -%}
{% if cookiecutter.add_clang_format -%}

## `clang-format`

The file `.clang-format` contains an initial configuration for (automatic) formatting with [clang-format](https://clang.llvm.org/docs/ClangFormat.html). Run the formatter with e.g.:

```shell
# dry run on main.c
clang-format -Werror --dry-run main.c

# format in place all *.c and *.h files under ./src
clang-format -i `find ./src -type f -name '*.[c|h]'`
```

{% endif -%}

## Acknowledgements

_This project was generated using [Cookiecutter](https://pypi.org/project/cookiecutter/). Thank you [@audreyfeldroy](https://github.com/audreyfeldroy) et al._
