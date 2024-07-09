WIP to deal with the nightmare that is building a C project.

```shell
# change into the build directory
cd build

# generate the build files
cmake ..

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
