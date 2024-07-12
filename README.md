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
  [1/6] What artifact(s) does the new project produce?
    1 - an executable
    2 - a library
    3 - both
    Choose from [1/2/3] (1): 
  [2/6] Do you want to organize components into subdirectories under src/? [y/n] (y): 
  [3/6] What is the name of the new project?
        Use [A-Za-z0-9_-.]+ (calculator): 
  [4/6] What should the build directory be called?
    1 - build
    2 - built
    3 - generated
    Choose from [1/2/3] (1): 
  [5/6] What should the directory that contains external dependencies be called?
    1 - external
    2 - third_party
    3 - lib
    4 - submodules
    5 - subprojects
    6 - My project doesn't have external dependencies
    Choose from [1/2/3/4/5/6] (1): 
  [6/6] Does the project use assets like images, sound, fonts, etc? [y/n] (y): 
```

Choosing default options as in the example above generates a layout like this with some
example files to get you started:

```txt
calculator/
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
├── external
│   ├── libtheirs
│   │   ├── include
│   │   │   ├── their_addition.h
│   │   │   └── their_subtraction.h
│   │   ├── src
│   │   │   ├── their_addition.c
│   │   │   └── their_subtraction.c
│   │   └── CMakeLists.txt
│   └── CMakeLists.txt
├── .clang-format
├── EMPTY
├── .gitignore
└── README.md
```

If you get a file named EMPTY in the root of the directory, that means the combination you chose hasn't been implemented yet.

