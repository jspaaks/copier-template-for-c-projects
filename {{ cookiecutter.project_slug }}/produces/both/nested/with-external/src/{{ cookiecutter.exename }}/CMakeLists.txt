cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/../..)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

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
        tgt_lib_{{ cookiecutter.libname }}
)

target_sources(
    tgt_exe_{{ cookiecutter.exename }}
    PRIVATE
        ${PROJECT_ROOT}/src/{{ cookiecutter.exename }}/main.c
)

install(TARGETS tgt_exe_{{ cookiecutter.exename }})
