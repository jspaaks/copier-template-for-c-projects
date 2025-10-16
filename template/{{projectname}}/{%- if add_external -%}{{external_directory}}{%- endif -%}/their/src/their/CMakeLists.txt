add_library(tgt_lib_their SHARED)

set_property(TARGET tgt_lib_their PROPERTY OUTPUT_NAME their)

target_include_directories(
    tgt_lib_their
    PRIVATE
        ../../include/
)

target_sources(
    tgt_lib_their
    PRIVATE
        addition.c
        subtraction.c
)

install(TARGETS tgt_lib_their)
