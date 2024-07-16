import os
from pathlib import Path
import shutil

def remove_assets():
    p = Path("assets")
    shutil.rmtree(p)

def remove_codeblocks():
    paths = [
        Path(".codeblocks"),
        Path("build", "codeblocks")
    ]
    for p in paths:
        shutil.rmtree(p)

def remove_cmake():
    paths = [
        Path("assets", "fonts", "CMakeLists.txt"),
        Path("assets", "images", "CMakeLists.txt"),
        Path("assets", "sounds", "CMakeLists.txt"),
        Path("assets", "CMakeLists.txt"),
        Path("build", "cmake"),
        Path("{{ cookiecutter.external_directory }}", "libtheirs", "CMakeLists.txt"),
        Path("{{ cookiecutter.external_directory }}", "CMakeLists.txt"),
        Path("src", "calculator", "CMakeLists.txt"),
        Path("src", "libours", "CMakeLists.txt"),
        Path("src", "CMakeLists.txt"),
        Path("CMakeLists.txt")
    ]
    for p in paths:
        shutil.rmtree(p) if os.path.isdir(p) else p.unlink(missing_ok=True)

def remove_external():
    p = Path("My project doesn't have external dependencies")
    shutil.rmtree(p)

def main():

    produces = "{{ cookiecutter.produces }}"
    wo_external = "{{ cookiecutter.external_directory }}" == "My project doesn't have external dependencies"
    wo_assets = "{{ cookiecutter.keep_assets }}" == "False"
    nested = "{{ cookiecutter.nested }}" == "True"
    wo_codeblocks = "{{ cookiecutter.add_codeblocks }}" == "False"
    wo_cmake = "{{ cookiecutter.add_cmake }}" == "False"

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
    if wo_cmake: remove_cmake()
    if wo_external: remove_external()


if __name__ == "__main__":
    main()
