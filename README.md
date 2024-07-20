# Cookiecutter template for C projects

Cookiecutter template for generating a somewhat generic project that can be built
with CMake and has the right configuration to be used in Code::Blocks editor.

To use, first install [cookiecutter from PyPI](https://pypi.org/project/cookiecutter/).

```shell
pipx install cookiecutter
```

Then run cookiecutter with this repo's URL as argument:

```shell
cookiecutter https://github.com/jspaaks/cookiecutter-codeblocks-cmake-c
```

Cookiecutter will then ask you a few questions, see the output below.

```text
  [1/12] What is the name of the new project?
        Use [A-Za-z0-9_-.]+ (calculator-project): 
  [2/12] What artifact(s) does the new project produce?
    1 - a library
    2 - an executable
    3 - both
    Choose from [1/2/3] (1): 
  [3/12] If any, what is the name of the library?
         Use [A-Za-z0-9_-.]+) (operations): 
  [4/12] If any, what is the name of the executable?
         Use [A-Za-z0-9_-.]+ (<Press enter to skip>): 
  [5/12] Do you want to organize components into subdirectories under src/? [y/n] (y): 
  [6/12] What should the build directory be called?
    1 - build
    2 - built
    3 - generated
    Choose from [1/2/3] (1): 
  [7/12] What should the directory that contains external dependencies be called?
    1 - external
    2 - third_party
    3 - lib
    4 - submodules
    5 - subprojects
    6 - My project doesn't have external dependencies
    Choose from [1/2/3/4/5/6] (1): 
  [8/12] Does the project use assets like images, sound, fonts, etc? [y/n] (y): 
  [9/12] Does the project use tests? [y/n] (y): 
  [10/12] Add a CMake build configuration? [y/n] (y): 
  [11/12] Add a Code::Blocks IDE configuration? [y/n] (y): 
  [12/12] Add a clang-format configuration? [y/n] (y): 
```

Choosing default options as in the example above generates a layout like this with some
example files to get you started:

```txt
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
