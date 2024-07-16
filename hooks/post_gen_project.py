import os
from pathlib import Path
import shutil

def remove_assets():
    p = Path("assets")
    shutil.rmtree(p)

def remove_external():
    p = Path("My project doesn't have external dependencies")
    shutil.rmtree(p)

def main():

    produces = "{{ cookiecutter.produces }}"
    wo_external = "{{ cookiecutter.external_directory }}" == "My project doesn't have external dependencies"
    wo_assets = "{{ cookiecutter.keep_assets }}" == "False"
    nested = "{{ cookiecutter.nested }}" == "True"

    base = Path(
        "produces",
        {
            "an executable": "exe",
            "a library": "lib",
            "both": "both"
        }[produces],
        "wo-external" if wo_external else "with-external",
        "nested" if nested else "flat"
    )
    srcs = [
        Path(base, ".codeblocks"),
        Path(base, "src"),
        Path(base, "CMakeLists.txt")
    ]
    if produces in ["a library", "both"]:
        srcs.append(Path(base, "include"))

    tgt = Path(".")
    for src in srcs:
        shutil.move(src, tgt)
    shutil.rmtree(Path("produces"))

    if wo_assets: remove_assets()
    if wo_external: remove_external()


if __name__ == "__main__":
    main()
