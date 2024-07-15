cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

{% if cookiecutter.keep_assets -%}
add_subdirectory(assets)
{% endif -%}

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
        ${CMAKE_CURRENT_LIST_DIR}/include/libours
)

target_sources(
    ours
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/libours/division.c
        ${CMAKE_CURRENT_LIST_DIR}/src/libours/multiplication.c
)

install(TARGETS ours)

