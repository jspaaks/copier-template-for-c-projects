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
🎤 What is the name of the new project? (Use [A-Za-z0-9_-.]+)
   calculator-project
🎤 Does the project produce an executable?
   Yes
🎤 What is the name of the executable? (Use [A-Za-z0-9_-.]+)
   calculator
🎤 Does the project produce a library?
   Yes
🎤 What is the name of the library? (Use [A-Za-z0-9_-.]+)
   operations
🎤 What is the purpose of the library?
   To facilitate testing and to be consumed by third parties
🎤 Do you want to organize components into subdirectories under src/?
   Yes
🎤 What should the build directory be called?
   build
🎤 Does the project have external dependencies?
   No
🎤 Does the project use assets like images, sound, fonts, etc?
   No
🎤 Does the project use tests?
   Yes
🎤 Add a CMake build configuration?
   Yes
🎤 Add a Code::Blocks IDE configuration?
   Yes
🎤 Add a clang-format configuration?
   Yes
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

The project should build out of the box using CMake

```shell
cd calculator-project/build/cmake
cmake ../..
```

Next run `make` to build the libary / executable / test executable

```shell
make
```

Then install (by default, to `calculator-project/build/cmake/dist`, can be configured by setting `CMAKE_INSTALL_PREFIX`)

```shell
make install
```

Run the executable with:

```shell
./dist/bin/calculator
```

Run the tests with:

```shell
./dist/bin/test_operations
./dist/bin/test_operations -j1 --verbose  # for easier to interpret output
```
