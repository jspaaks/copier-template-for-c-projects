# Copier template for C projects

Copier template for generating a somewhat generic C project that can be built
with CMake and has the right configuration to be used in Code::Blocks editor.

To use, first install [`copier` from PyPI](https://pypi.org/project/copier/).

```shell
pipx install copier
```

Then run `copier` with this repo's URL as argument:

```shell
copier copy https://github.com/jspaaks/cookiecutter-codeblocks-cmake-c
```

`copier` will then ask you a few questions, see the output below.

```text
TODO add questions
```

Choosing default options as in the example above generates a layout like this with some
example files to get you started:

```text
calculator-project/
├── assets
│   ├── fonts
│   │   ├── CMakeLists.txt
│   │   ├── font.ttf
│   │   └── README.md
│   ├── images
│   │   ├── CMakeLists.txt
│   │   ├── image.bmp
│   │   └── README.md
│   ├── sounds
│   │   ├── CMakeLists.txt
│   │   ├── README.md
│   │   └── sound.wav
│   └── CMakeLists.txt
├── build
│   ├── cmake
│   │   └── .gitkeep
│   ├── codeblocks
│   │   └── .gitkeep
│   └── .gitkeep
├── .codeblocks
│   ├── project.cbp
│   └── project.layout
├── external
│   ├── their
│   │   ├── include
│   │   │   └── their
│   │   │       ├── addition.h
│   │   │       └── subtraction.h
│   │   ├── src
│   │   │   └── their
│   │   │       ├── addition.c
│   │   │       └── subtraction.c
│   │   └── CMakeLists.txt
│   └── CMakeLists.txt
├── include
│   └── operations
│       ├── addition.h
│       ├── division.h
│       ├── multiplication.h
│       └── subtraction.h
├── src
│   └── operations
│       ├── addition.c
│       ├── CMakeLists.txt
│       ├── division.c
│       ├── multiplication.c
│       └── subtraction.c
├── test
│   └── operations
│       ├── CMakeLists.txt
│       ├── test_addition.c
│       ├── test_division.c
│       ├── test_multiplication.c
│       └── test_subtraction.c
├── .clang-format
├── CMakeLists.txt
├── .gitignore
└── README.md

21 directories, 39 files
```
