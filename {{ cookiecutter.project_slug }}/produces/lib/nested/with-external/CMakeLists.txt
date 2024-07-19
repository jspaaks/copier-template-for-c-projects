cmake_minimum_required(VERSION .21....28)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR})

project(project LANGUAGES C)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

add_subdirectory(${PROJECT_ROOT}/{{ cookiecutter.external_directory }}/libtheirs)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_library(tgt_{{ cookiecutter.libname }} SHARED)

set_property(TARGET tgt_{{ cookiecutter.libname }} PROPERTY OUTPUT_NAME {{ cookiecutter.libname }})

target_compile_definitions(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        $<$<CONFIGDebug>DEBUG>
)

target_compile_features(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        c_std_2
)

target_compile_options(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIGDebug>-g>
        $<$<CONFIGDebug>-O0>
        $<$<CONFIGRelease>-Werror>
)

target_include_directories(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/{{ cookiecutter.external_directory}}/libtheirs/include
        ${PROJECT_ROOT}/include
)

target_link_libraries(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        theirs
)

target_sources(
    tgt_{{ cookiecutter.libname }}
    PRIVATE
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/addition.c
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/division.c
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/multiplication.c
        ${PROJECT_ROOT}/src/{{ cookiecutter.libname }}/subtraction.c
)

install(TARGETS tgt_{{ cookiecutter.libname }})

{% if cookiecutter.add_test -%}
#
#
#

add_subdirectory(${PROJECT_ROOT}/test/{{ cookiecutter.libname }})
{% endif -%}
