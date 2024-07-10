# README.md

The project has been initialized with a dual configuration, 
1. a Code::Blocks IDE configuration in [.codeblocks/project.cbp](.codeblocks/project.cbp)
1. a [CMakeLists.txt](CMakeLists.txt) based configuration for building with CMake:

```shell
# change into the build directory
cd {{ cookiecutter.build_directory }}/cmake

# generate the build files
cmake ../..

# build the project
make

# install the project to <repo>/build/dist
make install

# run the program to see if it works
./dist/bin/program
```

Should output something like:

```text
-- test compile definitions
   DEBUG compile definition has been defined.

-- test whether header library was included
   a = 1

-- test wether math library was linked
   sqrt(144) = 12.000000

-- test c2x / c23 features
   0 1 2 3 4

-- test external library
   add(2, 3) = 5
```

_This project was generated using [Cookiecutter](https://pypi.org/project/cookiecutter/). Thank you [@audreyfeldroy](https://github.com/audreyfeldroy) et al._
