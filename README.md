# Cookiecutter template for Code::Blocks project

Cookiecutter template for generating a somewhat generic project that can be built
with CMake and has the right configuration to be used in Code::Blocks editor.

To use, first install [cookiecutter from PyPI](https://pypi.org/project/cookiecutter/)

```shell
pipx install cookiecutter
```

Then run cookiecutter with this repo's URL as argument:

```shell
cookiecutter https://github.com/jspaaks/cookiecutter-codeblocks-cmake-c
```

Choosing default options generates a layout like this:

```txt
.
└── template
    ├── .clang-format
    ├── CMakeLists.txt
    ├── .codeblocks
    │   └── project.cbp
    ├── external
    │   └── adding
    │       ├── CMakeLists.txt
    │       ├── include
    │       │   └── adding.h
    │       └── src
    │           └── adding.c
    ├── .gitignore
    ├── README.md
    └── src
        └── main.c
```
