cmake_minimum_required(VERSION 3.21...3.28)
project(project LANGUAGES C)
add_library(adding SHARED)
target_include_directories(
    adding
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/include/
)
target_sources(
    adding
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/adding.c
)
install(TARGETS adding)
