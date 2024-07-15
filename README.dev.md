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

|      |               |        |                                                                                        | checked    | state |
| ---  | ---           | ---    | ---                                                                                    | ---        | ---   |
| both | with-external | flat   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/with-external/flat)   | 2024-07-13 | ok |
| both | with-external | nested | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/with-external/nested) | 2024-07-13 | ok |
| both | wo-external   | flat   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/wo-external/flat)     | 2024-07-13 | ok |
| both | wo-external   | nested | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/both/wo-external/nested)   | 2024-07-13 | ok |
| exe  | with-external | flat   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/with-external/flat)    | 2024-07-13 | ok |
| exe  | with-external | nested | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/with-external/nested)  | 2024-07-13 | ok |
| exe  | wo-external   | flat   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/wo-external/flat)      | 2024-07-13 | ok |
| exe  | wo-external   | nested | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/exe/wo-external/nested)    | 2024-07-13 | ok |
| lib  | with-external | flat   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/with-external/flat)    | 2024-07-13 | ok |
| lib  | with-external | nested | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/with-external/nested)  | 2024-07-13 | ok |
| lib  | wo-external   | flat   | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/wo-external/flat)      | 2024-07-13 | EMPTY |
| lib  | wo-external   | nested | [link](%7B%7B%20cookiecutter.project_slug%20%7D%7D/produces/lib/wo-external/nested)    | 2024-07-13 | EMPTY |

When installing with assets, all combinations fail in 3. Fixable by making two `cmake ../..` calls, so might be problem with caching of CMAKE_INSTALL_PREFIX.
