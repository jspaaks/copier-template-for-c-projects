# Development notes

## checks

1. cmake runs
2. make runs
3. make install runs
4. dist/bin/calculator runs
5. ldd dist/lib/libours shows all linked
6. ldd dist/lib/libours shows all linked after moving dist
7. codeblocks project files opens
8. file exists for every file in codeblocks filetree
9. codeblocks project builds
10. codeblocks project runs
11. tests run

## results 

|      |        |               |                                                                                        | checked    | state |
| ---  | ---    | ---           | ---                                                                                    | ---        | ---   |
| both | flat   | with-external | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/with-external/flat)   | 2024-07-19 | ok    |
| both | flat   | wo-external   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/wo-external/flat)     | 2024-07-19 | ok    |
| both | nested | with-external | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/with-external/nested) | 2024-07-19 | ok    |
| both | nested | wo-external   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/wo-external/nested)   | 2024-07-19 | ok    |
| exe  | flat   | with-external | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/with-external/flat)    | 2024-07-19 | ok    |
| exe  | flat   | wo-external   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/wo-external/flat)      | 2024-07-19 | ok    |
| exe  | nested | with-external | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/with-external/nested)  | 2024-07-19 | ok    |
| exe  | nested | wo-external   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/wo-external/nested)    | 2024-07-19 | ok    |
| lib  | flat   | with-external | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/with-external/flat)    | 2024-07-17 | ?     |
| lib  | flat   | wo-external   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/wo-external/flat)      | 2024-07-17 | ?     |
| lib  | nested | with-external | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/with-external/nested)  | 2024-07-17 | ?     |
| lib  | nested | wo-external   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/wo-external/nested)    | 2024-07-17 | ?     |

## TODO

1. review usage of `#include "libcalculator/addition.h"` vs `#include "calculator/addition.h"`
1. consider setting PROJECT_ROOT in CMakeLists.txt files and using it in all paths
1. review usage of `-I../../include/libcalculator` with `#include "addition.h"` vs. `-I../../include` with `#include "libcalculator/addition.h"`
1. rename target for theirs to be consistent with the other targets
1. add test files to codeblocks project config file as Unit
1. add test target to codeblocks project files for building the ./tests binary

1. add more testing framework(s), e.g.
   1. googletest [https://github.com/google/googletest](https://github.com/google/googletest)
   1. check [https://github.com/libcheck/check/](https://github.com/libcheck/check/), [https://libcheck.github.io/check/](https://libcheck.github.io/check/)
   1. ~kyua~ [https://github.com/freebsd/kyua](https://github.com/freebsd/kyua)
   1. Unity [https://www.throwtheswitch.org/unity](https://www.throwtheswitch.org/unity), [https://github.com/ThrowTheSwitch/Unity](https://github.com/ThrowTheSwitch/Unity)
   1. CMocka? [https://lwn.net/Articles/558106/](https://lwn.net/Articles/558106/)
   1. Catch2?
   1. acutest?
1. review necessity of rpath for combinations that have one level of indirection in their libraries
1. review virtual target when there is just one target
1. review usage of multiple `project` across nested CMakeLists.txt
1. review usage of multiple CMAKE_BUILD_TYPE and CMAKE_INSTALL_PREFIX across nested CMakeLists.txt
1. review strategy for when to split into multiple CMakeLists.txt (affects where files like libcalculator.so are produced under build/cmake in turn affecting link flags)
1. add CMakeLists.txt to include so they can be installed
