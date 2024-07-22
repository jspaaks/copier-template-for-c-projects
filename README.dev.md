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
| both | flat   | with-external | [link](%7B%7B%20project_slug%20%7D%7D/produces/both/with-external/flat)   | 2024-07-22 | ok      |
| both | flat   | wo-external   | [link](%7B%7B%20project_slug%20%7D%7D/produces/both/wo-external/flat)     | 2024-07-22 | ok      |
| both | nested | with-external | [link](%7B%7B%20project_slug%20%7D%7D/produces/both/with-external/nested) | 2024-07-22 | ok      |
| both | nested | wo-external   | [link](%7B%7B%20project_slug%20%7D%7D/produces/both/wo-external/nested)   | 2024-07-20 | ?       |
| exe  | flat   | with-external | [link](%7B%7B%20project_slug%20%7D%7D/produces/exe/with-external/flat)    | 2024-07-20 | ?       |
| exe  | flat   | wo-external   | [link](%7B%7B%20project_slug%20%7D%7D/produces/exe/wo-external/flat)      | 2024-07-20 | ?       |
| exe  | nested | with-external | [link](%7B%7B%20project_slug%20%7D%7D/produces/exe/with-external/nested)  | 2024-07-20 | ?       |
| exe  | nested | wo-external   | [link](%7B%7B%20project_slug%20%7D%7D/produces/exe/wo-external/nested)    | 2024-07-20 | ?       |
| lib  | flat   | with-external | [link](%7B%7B%20project_slug%20%7D%7D/produces/lib/with-external/flat)    | 2024-07-20 | ?       |
| lib  | flat   | wo-external   | [link](%7B%7B%20project_slug%20%7D%7D/produces/lib/wo-external/flat)      | 2024-07-20 | ?       |
| lib  | nested | with-external | [link](%7B%7B%20project_slug%20%7D%7D/produces/lib/with-external/nested)  | 2024-07-20 | ?       |
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
