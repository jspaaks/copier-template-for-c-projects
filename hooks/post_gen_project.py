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

def main():

    produces = "{{ cookiecutter.produces }}"
    exename = "{{ cookiecutter.exename }}"
    libname = "{{ cookiecutter.libname }}"
    wo_external = "{{ cookiecutter.external_directory }}" == "My project doesn't have external dependencies"
    wo_assets = "{{ cookiecutter.add_assets }}" == "False"
    nested = "{{ cookiecutter.nested }}" == "True"
    wo_codeblocks = "{{ cookiecutter.add_codeblocks }}" == "False"
    wo_cmake = "{{ cookiecutter.add_cmake }}" == "False"
    wo_clang_format = "{{ cookiecutter.add_clang_format }}" == "False"

    ENTER_TO_SKIP = "<Press enter to skip>"
    if produces == "an executable":
        assert exename != ENTER_TO_SKIP, "Expected executable name to not be empty / <Press enter to skip>"
        assert libname == ENTER_TO_SKIP, "Expected library name to be empty / <Press enter to skip>"
    elif produces == "a library":
        assert exename == ENTER_TO_SKIP, "Expected executable name to be empty / <Press enter to skip>"
        assert libname != ENTER_TO_SKIP, "Expected library name to not be empty / <Press enter to skip>"
        assert libname[:3] == "lib", "Expected library name to start with 'lib' but was {}".format(libname)
    elif produces == "both":
        assert exename != ENTER_TO_SKIP, "Expected executable name to not be empty / <Press enter to skip>"
        assert libname != ENTER_TO_SKIP, "Expected library name to not be empty / <Press enter to skip>"
        assert libname[:3] == "lib", "Expected library name to start with 'lib' but was {}".format(libname)


    src = Path(
        "produces",
        {
            "an executable": "exe",
            "a library": "lib",
            "both": "both"
        }[produces],
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


if __name__ == "__main__":
    main()
