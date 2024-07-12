cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/{{ cookiecutter.external_directory }})

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_executable(calculator)

target_compile_definitions(
    calculator
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    calculator
    PRIVATE
        c_std_23
)

target_compile_options(
    calculator
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    calculator
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/{{ cookiecutter.external_directory }}/their/include
)

target_link_libraries(
    calculator
    PRIVATE
        m
        their
)

target_sources(
    calculator
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src/addition.c
        ${CMAKE_CURRENT_LIST_DIR}/src/division.c
        ${CMAKE_CURRENT_LIST_DIR}/src/main.c
        ${CMAKE_CURRENT_LIST_DIR}/src/multiplication.c
        ${CMAKE_CURRENT_LIST_DIR}/src/subtraction.c
)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

install(TARGETS calculator)

