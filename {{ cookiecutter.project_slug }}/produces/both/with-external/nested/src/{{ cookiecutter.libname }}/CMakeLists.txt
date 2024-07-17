cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_library(tgt_{{ cookiecutter.libname }} SHARED)

set_property(TARGET tgt_{{ cookiecutter.libname }} PROPERTY OUTPUT_NAME {{ cookiecutter.libname[3:] }})

target_compile_definitions(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        c_std_23
)

target_compile_options(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/../../include/{{ cookiecutter.libname }}
        ${CMAKE_CURRENT_LIST_DIR}/../../{{ cookiecutter.external_directory }}/libtheirs/include
)

target_link_libraries(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        theirs
)

target_sources(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/addition.c
        ${CMAKE_CURRENT_LIST_DIR}/division.c
        ${CMAKE_CURRENT_LIST_DIR}/multiplication.c
        ${CMAKE_CURRENT_LIST_DIR}/subtraction.c
)

install(TARGETS tgt_{{ cookiecutter.libname }})
