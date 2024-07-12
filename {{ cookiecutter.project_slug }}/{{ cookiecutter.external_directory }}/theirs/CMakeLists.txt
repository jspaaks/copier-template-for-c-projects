cmake_minimum_required(VERSION 3.21...3.28)
project(project LANGUAGES C)
add_library(theirs SHARED)
target_include_directories(
    theirs
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/include/
)
target_sources(
    theirs
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/their_addition.c
        ${CMAKE_CURRENT_LIST_DIR}/src/their_subtraction.c
)
install(TARGETS theirs)
