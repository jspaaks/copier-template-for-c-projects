cmake_minimum_required(VERSION 3.23...3.28)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/..)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

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
)

target_sources(
    tgt_lib_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/src/division.c
        ${PROJECT_ROOT}/src/multiplication.c
    PUBLIC
        FILE_SET fset_lib_{{ cookiecutter.libname }}_headers
        TYPE HEADERS
        BASE_DIRS
            ${PROJECT_ROOT}/include
        FILES
            ${PROJECT_ROOT}/include/division.h
            ${PROJECT_ROOT}/include/multiplication.h
)

install(TARGETS tgt_lib_{{ cookiecutter.libname }}
    LIBRARY
    FILE_SET fset_lib_{{ cookiecutter.libname }}_headers
)
