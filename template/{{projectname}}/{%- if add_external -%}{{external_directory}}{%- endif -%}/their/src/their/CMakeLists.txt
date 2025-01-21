cmake_minimum_required(VERSION 3.21...3.28)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/../..)

add_library(tgt_lib_their SHARED)

set_property(TARGET tgt_lib_their PROPERTY OUTPUT_NAME their)

target_include_directories(
    tgt_lib_their
    PRIVATE
        ${PROJECT_ROOT}/include/
)

target_sources(
    tgt_lib_their
    PRIVATE
        ${PROJECT_ROOT}/src/their/addition.c
        ${PROJECT_ROOT}/src/their/subtraction.c
)

install(TARGETS tgt_lib_their)
