set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR}/../..)

list(APPEND CMAKE_INSTALL_RPATH $ORIGIN $ORIGIN/../lib)

add_executable(tgt_exe_test_{{ libname }})

set_property(TARGET tgt_exe_test_{{ libname }} PROPERTY OUTPUT_NAME test_{{ libname }})

target_compile_definitions(
    tgt_exe_test_{{ libname }}
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG>
)

target_compile_features(
    tgt_exe_test_{{ libname }}
    PRIVATE
        c_std_23
)

target_compile_options(
    tgt_exe_test_{{ libname }}
    PRIVATE
        -Wall
        -Wextra
        -pedantic
        $<$<CONFIG:Debug>:-g>
        $<$<CONFIG:Debug>:-O0>
        $<$<CONFIG:Release>:-Werror>
)

target_include_directories(
    tgt_exe_test_{{ libname }}
    PRIVATE
        ${PROJECT_ROOT}/include
)

target_link_libraries(
    tgt_exe_test_{{ libname }}
    PRIVATE
        criterion
        tgt_lib_{{ libname }}
)

target_sources(
    tgt_exe_test_{{ libname }}
    PRIVATE
        ${PROJECT_ROOT}/test/{{ libname }}/test_addition.c
        ${PROJECT_ROOT}/test/{{ libname }}/test_division.c
        ${PROJECT_ROOT}/test/{{ libname }}/test_multiplication.c
        ${PROJECT_ROOT}/test/{{ libname }}/test_subtraction.c
)

install(TARGETS tgt_exe_test_{{ libname }})
