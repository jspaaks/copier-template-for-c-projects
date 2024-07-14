cmake_minimum_required(VERSION 3.21...3.28)

project(project LANGUAGES C)

{% if cookiecutter.keep_assets -%}
add_subdirectory(assets)
{% endif -%}
add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/{{ cookiecutter.external_directory }}/libtheirs)
add_subdirectory(src/calculator)
add_subdirectory(src/libours)
