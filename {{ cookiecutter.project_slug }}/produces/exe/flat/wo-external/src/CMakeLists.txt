cmake_minimum_required(VERSION 3.21...3.28)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/..)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

add_executable(tgt_exe_{{ cookiecutter.exename }})

set_property(TARGET tgt_exe_{{ cookiecutter.exename }} PROPERTY OUTPUT_NAME {{ cookiecutter.exename }})

target_compile_definitions(
    tgt_exe_{{ cookiecutter.exename }}
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    tgt_exe_{{ cookiecutter.exename }}
    PRIVATE
        c_std_23
)

target_compile_options(
    tgt_exe_{{ cookiecutter.exename }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    tgt_exe_{{ cookiecutter.exename }}
    PRIVATE
        ${PROJECT_ROOT}/include
)

target_link_libraries(
    tgt_exe_{{ cookiecutter.exename }}
    PRIVATE
        m
)

target_sources(
    tgt_exe_{{ cookiecutter.exename }}
    PRIVATE
        ${PROJECT_ROOT}/src/division.c
        ${PROJECT_ROOT}/src/main.c
        ${PROJECT_ROOT}/src/multiplication.c
)

install(TARGETS tgt_exe_{{ cookiecutter.exename }})
