# Cookiecutter template for Code::Blocks project

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
  [1/11] What is the name of the new project?
        Use [A-Za-z0-9_-.]+ (calculator-project): 
  [2/11] What artifact(s) does the new project produce?
    1 - an executable
    2 - a library
    3 - both
    Choose from [1/2/3] (1): 
  [3/11] If any, what is the name of the executable?
         Use [A-Za-z0-9_-.]+ (calculator): 
  [4/11] If any, what is the name of the library?
         Use lib[A-Za-z0-9_-.]+) (<Press enter to skip>): 
  [5/11] Do you want to organize components into subdirectories under src/? [y/n] (y): 
  [6/11] What should the build directory be called?
    1 - build
    2 - built
    3 - generated
    Choose from [1/2/3] (1): 
  [7/11] What should the directory that contains external dependencies be called?
    1 - external
    2 - third_party
    3 - lib
    4 - submodules
    5 - subprojects
    6 - My project doesn't have external dependencies
    Choose from [1/2/3/4/5/6] (1): 
  [8/11] Does the project use assets like images, sound, fonts, etc? [y/n] (y): 
  [9/11] Add a CMake build configuration? [y/n] (y): 
  [10/11] Add a Code::Blocks IDE configuration? [y/n] (y): 
  [11/11] Add a clang-format configuration? [y/n] (y): 
```

Choosing default options as in the example above generates a layout like this with some
example files to get you started:

```txt
calculator-project/
├── assets
│   ├── CMakeLists.txt
│   ├── fonts
│   │   ├── CMakeLists.txt
│   │   ├── font.ttf
│   │   └── README.md
│   ├── images
│   │   ├── CMakeLists.txt
│   │   ├── image.bmp
│   │   └── README.md
│   └── sounds
│       ├── CMakeLists.txt
│       ├── README.md
│       └── sound.wav
├── build
│   ├── cmake
│   └── codeblocks
├── CMakeLists.txt
├── external
│   ├── CMakeLists.txt
│   └── libtheirs
│       ├── CMakeLists.txt
│       ├── include
│       │   ├── their_addition.h
│       │   └── their_subtraction.h
│       └── src
│           ├── their_addition.c
│           └── their_subtraction.c
├── README.md
└── src
    └── calculator
        ├── addition.c
        ├── addition.h
        ├── division.c
        ├── division.h
        ├── main.c
        ├── multiplication.c
        ├── multiplication.h
        ├── subtraction.c
        └── subtraction.h

14 directories, 27 files
```
