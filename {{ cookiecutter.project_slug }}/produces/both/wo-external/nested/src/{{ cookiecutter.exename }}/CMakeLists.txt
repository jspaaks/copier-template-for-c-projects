cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_executable(tgt_{{ cookiecutter.exename }})

set_property(TARGET tgt_{{ cookiecutter.exename }} PROPERTY OUTPUT_NAME {{ cookiecutter.exename }})

target_compile_definitions(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        c_std_23
)

target_compile_options(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/../../include/{{ cookiecutter.libname }}
)

target_link_libraries(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        m
        tgt_{{ cookiecutter.libname }}
)

target_sources(
    tgt_{{ cookiecutter.exename }}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/main.c
)

install(TARGETS tgt_{{ cookiecutter.exename }})
