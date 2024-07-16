cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/{{ cookiecutter.external_directory }}/libtheirs)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_library(ours SHARED)

target_compile_definitions(
    ours
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    ours
    PRIVATE
        c_std_23
)

target_compile_options(
    ours
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    ours
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/{{ cookiecutter.external_directory}}/libtheirs/include
        ${CMAKE_CURRENT_LIST_DIR}/include/libours
)

target_link_libraries(
    ours
    PRIVATE
        theirs
)

target_sources(
    ours
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/libours/addition.c
        ${CMAKE_CURRENT_LIST_DIR}/src/libours/division.c
        ${CMAKE_CURRENT_LIST_DIR}/src/libours/multiplication.c
        ${CMAKE_CURRENT_LIST_DIR}/src/libours/subtraction.c
)

install(TARGETS ours)
