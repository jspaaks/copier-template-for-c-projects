cmake_minimum_required(VERSION 3.21...3.28)
project(project LANGUAGES C)
add_library(subtraction SHARED)
target_include_directories(
    subtraction
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/include/
)
target_sources(
    subtraction
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/subtraction.c
)
install(TARGETS subtraction)
