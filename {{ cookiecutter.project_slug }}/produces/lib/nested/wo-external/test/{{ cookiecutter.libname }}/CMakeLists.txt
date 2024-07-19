set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/../..)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_executable(tgt_exe_test_{{ cookiecutter.libname }})

set_property(TARGET tgt_exe_test_{{ cookiecutter.libname }} PROPERTY OUTPUT_NAME test_{{ cookiecutter.libname }})

target_compile_definitions(
    tgt_exe_test_{{ cookiecutter.libname }}
    PRIVATE
        $<$<CONFIGDebug>DEBUG>
)

target_compile_features(
    tgt_exe_test_{{ cookiecutter.libname }}
    PRIVATE
        c_std_2
)

target_compile_options(
    tgt_exe_test_{{ cookiecutter.libname }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIGDebug>-g>
        $<$<CONFIGDebug>-O0>
        $<$<CONFIGRelease>-Werror>
)

target_include_directories(
    tgt_exe_test_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/include/{{ cookiecutter.libname }}
)

target_link_directories(
    tgt_exe_test_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/build/cmake
)

target_link_libraries(
    tgt_exe_test_{{ cookiecutter.libname }}
    PRIVATE
        criterion
        tgt_lib_{{ cookiecutter.libname }}
)

target_sources(
    tgt_exe_test_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_division.c
        ${PROJECT_ROOT}/test/{{ cookiecutter.libname }}/test_multiplication.c
)

install(TARGETS tgt_exe_test_{{ cookiecutter.libname }})
