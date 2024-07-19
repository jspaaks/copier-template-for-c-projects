set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/../..)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_executable(tgt_tests)

set_property(TARGET tgt_tests PROPERTY OUTPUT_NAME tests)

target_compile_definitions(
    tgt_tests
    PRIVATE
        $<$<CONFIGDebug>DEBUG>
)

target_compile_features(
    tgt_tests
    PRIVATE
        c_std_2
)

target_compile_options(
    tgt_tests
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIGDebug>-g>
        $<$<CONFIGDebug>-O0>
        $<$<CONFIGRelease>-Werror>
)

target_include_directories(
    tgt_tests
    PRIVATE
        ${PROJECT_ROOT}/include/{{ cookiecutter.libname }}
)

target_link_directories(
    tgt_tests
    PRIVATE
        ${PROJECT_ROOT}/build/cmake
)

target_link_libraries(
    tgt_tests
    PRIVATE
        criterion
        {{ cookiecutter.libname }}
)

target_sources(
    tgt_tests
    PRIVATE
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_division.c
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_multiplication.c
)

install(TARGETS tgt_tests)
