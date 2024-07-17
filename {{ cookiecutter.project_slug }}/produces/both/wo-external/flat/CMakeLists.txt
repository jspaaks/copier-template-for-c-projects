cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

{% if cookiecutter.add_assets -%}
add_subdirectory(assets)

{% endif -%}

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_executable(tgt_{{ cookiecutter.exename }})

set_property(TARGET tgt_{{ cookiecutter.exename }} PROPERTY OUTPUT_NAME {{ cookiecutter.exename }})

target_compile_definitions(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        c_std_23
)

target_compile_options(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/include
)

target_link_libraries(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        m
        tgt_{{ cookiecutter.libname }}
)

target_sources(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/main.c
)

install(TARGETS tgt_{{ cookiecutter.exename }})

#
#
#
#
#
#

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
        ${CMAKE_CURRENT_LIST_DIR}/include
)

target_sources(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/division.c
        ${CMAKE_CURRENT_LIST_DIR}/src/multiplication.c
)

install(TARGETS tgt_{{ cookiecutter.libname }})

