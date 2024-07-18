set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/../..)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_executable(tgt_tests)

set_property(TARGET tgt_tests PROPERTY OUTPUT_NAME tests)

target_compile_definitions(
    tgt_tests
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    tgt_tests
    PRIVATE
        c_std_23
)

target_compile_options(
    tgt_tests
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    tgt_tests
    PRIVATE
        ${PROJECT_ROOT}/include
)

target_link_directories(
    tgt_tests
    PRIVATE
        ${PROJECT_ROOT}/build/cmake/src/{{ cookiecutter.libname }}
)

target_link_libraries(
    tgt_tests
    PRIVATE
        criterion
        {{ cookiecutter.libname[3:] }}
)

target_sources(
    tgt_tests
    PRIVATE
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_addition.c
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_division.c
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_multiplication.c
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_subtraction.c
)

install(TARGETS tgt_tests)
