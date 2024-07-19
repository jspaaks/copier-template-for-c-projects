cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/../..)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_library(tgt_lib_{{ cookiecutter.libname }} SHARED)

set_property(TARGET tgt_lib_{{ cookiecutter.libname }} PROPERTY OUTPUT_NAME {{ cookiecutter.libname }})

target_compile_definitions(
    tgt_lib_{{ cookiecutter.libname }}
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    tgt_lib_{{ cookiecutter.libname }}
    PRIVATE
        c_std_23
)

target_compile_options(
    tgt_lib_{{ cookiecutter.libname }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    tgt_lib_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/include
        ${PROJECT_ROOT}/{{ cookiecutter.external_directory }}/libtheirs/include
)

target_link_libraries(
    tgt_lib_{{ cookiecutter.libname }}
    PRIVATE
        theirs
)

target_sources(
    tgt_lib_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/addition.c
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/division.c
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/multiplication.c
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/subtraction.c
)

install(TARGETS tgt_lib_{{ cookiecutter.libname }})
