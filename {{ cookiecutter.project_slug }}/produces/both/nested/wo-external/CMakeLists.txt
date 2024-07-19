cmake_minimum_required(VERSION 3.21...3.28)

set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR})

project(project LANGUAGES C)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set_property(CACHE CMAKE_INSTALL_PREFIX PROPERTY VALUE "${CMAKE_BINARY_DIR}/dist")
endif()

{% if cookiecutter.add_assets -%}
add_subdirectory(${PROJECT_ROOT}/assets)

{% endif -%}
add_subdirectory(${PROJECT_ROOT}/src/{{ cookiecutter.exename }})

add_subdirectory(${PROJECT_ROOT}/src/{{ cookiecutter.libname }})
{% if cookiecutter.add_test -%}

add_subdirectory(${PROJECT_ROOT}/test/{{ cookiecutter.libname }})
{% endif -%}
