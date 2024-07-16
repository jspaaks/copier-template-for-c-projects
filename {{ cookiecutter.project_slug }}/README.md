# README.md

The project has been initialized with a dual configuration, 
1. a Code::Blocks IDE configuration in [.codeblocks/project.cbp](.codeblocks/project.cbp)
1. a [CMakeLists.txt](CMakeLists.txt)-based configuration for building with CMake:

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

_This project was generated using [Cookiecutter](https://pypi.org/project/cookiecutter/). Thank you [@audreyfeldroy](https://github.com/audreyfeldroy) et al._
