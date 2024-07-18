import os
from pathlib import Path
import shutil

def remove_assets():
    p = Path("assets")
    shutil.rmtree(p)

def remove_cmake():
    paths = [
        Path("assets", "fonts", "CMakeLists.txt"),
        Path("assets", "images", "CMakeLists.txt"),
        Path("assets", "sounds", "CMakeLists.txt"),
        Path("assets", "CMakeLists.txt"),
        Path("{{ cookiecutter.build_directory }}", "cmake"),
        Path("{{ cookiecutter.external_directory }}", "libtheirs", "CMakeLists.txt"),
        Path("{{ cookiecutter.external_directory }}", "CMakeLists.txt"),
        Path("src", "calculator", "CMakeLists.txt"),
        Path("src", "libours", "CMakeLists.txt"),
        Path("src", "CMakeLists.txt"),
        Path("CMakeLists.txt")
    ]
    for p in paths:
        shutil.rmtree(p) if os.path.isdir(p) else p.unlink(missing_ok=True)

def remove_codeblocks():
    paths = [
        Path(".codeblocks"),
        Path("{{ cookiecutter.build_directory }}", "codeblocks")
    ]
    for p in paths:
        shutil.rmtree(p)

def remove_clang_format():
    Path(".clang-format").unlink()

def remove_external():
    p = Path("My project doesn't have external dependencies")
    shutil.rmtree(p)

def remove_test():
    p = Path("test")
    shutil.rmtree(p)

def main():

    produceslib = "{{ cookiecutter.produces }}" in ["a library", "both"]
    producesexe = "{{ cookiecutter.produces }}" in ["an executable", "both"]
    exename = "{{ cookiecutter.exename }}"
    libname = "{{ cookiecutter.libname }}"
    wo_external = "{{ cookiecutter.external_directory }}" == "My project doesn't have external dependencies"
    wo_assets = "{{ cookiecutter.add_assets }}" == "False"
    wo_test = "{{ cookiecutter.add_test }}" == "False"
    wo_codeblocks = "{{ cookiecutter.add_codeblocks }}" == "False"
    wo_cmake = "{{ cookiecutter.add_cmake }}" == "False"
    wo_clang_format = "{{ cookiecutter.add_clang_format }}" == "False"
    nested = "{{ cookiecutter.nested }}" == "True"


    EMPTYVALUE = "<Press enter to skip>"
    if not produceslib and libname != EMPTYVALUE:
        print("\nExpected library name to be empty but was '{}'.\n".format(libname))
        return 1
    if produceslib and libname[:3] != "lib":
        print("\nExpected library name to start with 'lib' but was '{}'.\n".format(libname))
        return 1

    if not producesexe and exename != EMPTYVALUE:
        print("\nExpected executable name to be empty but was '{}'.\n".format(exename))
        return 1

    if not produceslib and not wo_test:
        print("\nProject doesn't produce a library to test against.\n")
        return 1

    src = Path(
        "produces",
        {
            (True, False): "exe",
            (False, True): "lib",
            (True, True): "both"
        }[(producesexe, produceslib)],
        "wo-external" if wo_external else "with-external",
        "nested" if nested else "flat"
    )
    tgt = Path(".")
    shutil.copytree(src, tgt, dirs_exist_ok=True)
    shutil.rmtree(Path("produces"))

    if wo_assets: remove_assets()
    if wo_codeblocks: remove_codeblocks()
    if wo_clang_format: remove_clang_format()
    if wo_cmake: remove_cmake()
    if wo_external: remove_external()
    if wo_test: remove_test()


if __name__ == "__main__":
    rc = main()
    exit(rc)
