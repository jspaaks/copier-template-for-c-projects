cmake_minimum_required(VERSION 3.21...3.28)
project(project LANGUAGES C)
add_library(addition SHARED)
target_include_directories(
    addition
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/include/
)
target_sources(
    addition
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/addition.c
)
install(TARGETS addition)
