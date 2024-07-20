cmake_minimum_required(VERSION 3.23...3.28)

project(project LANGUAGES C)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR})

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

{% if cookiecutter.add_assets -%}
add_subdirectory(${PROJECT_ROOT}/assets)
{% endif -%}
add_subdirectory(${PROJECT_ROOT}/{{ cookiecutter.external_directory }}/their)
add_subdirectory(${PROJECT_ROOT}/src/{{ cookiecutter.exename }})

