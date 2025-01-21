# Copier template for C projects

Copier template for generating a generic C project that can be built
with CMake.

To use, first install [`copier` from PyPI](https://pypi.org/project/copier/).

```shell
pipx install copier
```

Then run `copier` with this repo's URL as argument:

```shell
# use a dot at the end for generating in the current directory,
# or replace it with a path of your choosing
copier copy https://github.com/jspaaks/copier-template-for-c-projects .
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
   Yes
🎤 What should the directory that contains external dependencies be called?
   external
🎤 Does the project use assets like images, sound, fonts, etc?
   Yes
🎤 Does the project use tests?
   Yes
🎤 What C standard does the project use?
   C23
🎤 Add a clang-format configuration?
   Yes
🎤 Do you want to include a copy of the answers you just provided as .copier-answers.yml?
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
│   └── .gitkeep
├── external
│   ├── their
│   │   ├── include
│   │   │   └── their
│   │   │       ├── addition.h
│   │   │       └── subtraction.h
│   │   ├── src
│   │   │   └── their
│   │   │       ├── addition.c
│   │   │       ├── CMakeLists.txt
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
│   ├── calculator
│   │   ├── CMakeLists.txt
│   │   └── main.c
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

19 directories, 38 files
```

The generated project should build out of the box using CMake:

```shell
cd calculator-project/build/
cmake ..
```

Next, build the libary / executable / test executable:

```shell
cmake --build .
```

Then install (by default, to `calculator-project/build/dist`, can be configured by
setting `CMAKE_INSTALL_PREFIX` when calling `cmake`):

```shell
cmake --install .
```

If you configured your project to build an executable, you can run it with:

```shell
./dist/bin/calculator
```

If you configured your project to include tests, you can run them with:

```shell
./dist/bin/test_operations
./dist/bin/test_operations -j1 --verbose  # for easier-to-interpret output
```
