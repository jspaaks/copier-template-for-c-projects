# Development notes

## checks

1. cmake runs
2. make runs
3. make install runs
4. dist/bin/calculator runs
5. dist/bin/test_operations runs
6. ldd dist/lib/liboperations shows all linked
7. ldd dist/lib/liboperations shows all linked after moving dist
8. codeblocks project files opens
9. file exists for every file in codeblocks filetree
10. codeblocks project builds
11. codeblocks project runs

## results 

|      |        |               |                                                                           | checked    | state   |
| ---  | ---    | ---           | ---                                                                       | ---        | ---     |
| both | flat   | with-external |                                                                           | 2024-07-22 | ok      |
| both | flat   | wo-external   |                                                                           | 2024-07-22 | ok      |
| both | nested | with-external |                                                                           | 2024-07-22 | ok      |
| both | nested | wo-external   |                                                                           | 2024-07-22 | ok      |
| exe  | flat   | with-external |                                                                           | 2024-07-22 | ok      |
| exe  | flat   | wo-external   |                                                                           | 2024-07-22 | ok      |
| exe  | nested | with-external |                                                                           | 2024-07-22 | ok      |
| exe  | nested | wo-external   |                                                                           | 2024-07-22 | ok      |
| lib  | flat   | with-external |                                                                           | 2024-07-22 | ok      |
| lib  | flat   | wo-external   |                                                                           | 2024-07-22 | ok      |
| lib  | nested | with-external |                                                                           | 2024-07-22 | ok      |
| lib  | nested | wo-external   | [link](%7B%7B%20project_slug%20%7D%7D/produces/lib/wo-external/nested)    | 2024-07-20 | ?       |

## TODO

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
1. review usage of multiple CMAKE_BUILD_TYPE and CMAKE_INSTALL_PREFIX across nested CMakeLists.txt
1. review usage of `#include "operations_addition.h"` for flat trees
1. lib-flat-witrh-external doesnt have .codeblocks/project.layout
1. lib-nest-with-external/src/addition.c is missing its own include header
1. lib-nest-with-external/src/multiplication.c is missing its own include header
1. lib-nest-with-external/src/subtraction.c is missing its own include header