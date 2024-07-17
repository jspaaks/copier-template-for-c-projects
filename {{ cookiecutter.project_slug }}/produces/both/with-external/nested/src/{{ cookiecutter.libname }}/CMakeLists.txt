cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

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
        ${CMAKE_CURRENT_LIST_DIR}/../../include/libours
        ${CMAKE_CURRENT_LIST_DIR}/../../{{ cookiecutter.external_directory }}/libtheirs/include
)

target_link_libraries(
    ours
    PRIVATE
        theirs
)

target_sources(
    ours
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/addition.c
        ${CMAKE_CURRENT_LIST_DIR}/division.c
        ${CMAKE_CURRENT_LIST_DIR}/multiplication.c
        ${CMAKE_CURRENT_LIST_DIR}/subtraction.c
)

install(TARGETS ours)
