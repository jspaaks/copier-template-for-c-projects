cmake_minimum_required(VERSION 3.21...3.28)
project(project LANGUAGES C)
add_library(tgt_lib_their SHARED)
set_property(TARGET tgt_lib_their PROPERTY OUTPUT_NAME their)
target_include_directories(
    tgt_lib_their
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/include/
)
target_sources(
    tgt_lib_their
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/their/addition.c
        ${CMAKE_CURRENT_LIST_DIR}/src/their/subtraction.c
)
install(TARGETS tgt_lib_their)
