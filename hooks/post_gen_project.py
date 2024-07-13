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

    # derived booleans
    both = produces == "both"
    exe = produces == "an executable"
    lib = produces == "a library"
    with_external = not wo_external
    flat = not nested

    if wo_assets: remove_assets()
    if wo_external: remove_external()

    srcs = []

    if both:
        if with_external:
            if flat:
                base = Path("produces", "both", "with-external", "flat")
                srcs = [
                    Path(base, "EMPTY")
                ]
            elif nested:
                base = Path("produces", "both", "with-external", "nested")
                srcs = [
                    Path(base, ".codeblocks"),
                    Path(base, "include"),
                    Path(base, "src"),
                    Path(base, "CMakeLists.txt")
                ]
        elif wo_external:
            if flat:
                base = Path("produces", "both", "wo-external", "flat")
                srcs = [
                    Path(base, "EMPTY")
                ]
            elif nested:
                base = Path("produces", "both", "wo-external", "nested")
                srcs = [
                    Path(base, ".codeblocks"),
                    Path(base, "include"),
                    Path(base, "src"),
                    Path(base, "CMakeLists.txt")
                ]
    elif exe:
        if with_external:
            if flat:
                base = Path("produces", "exe", "with-external", "flat")
                srcs = [
                    Path(base, ".codeblocks"),
                    Path(base, "src"),
                    Path(base, "CMakeLists.txt")
                ]
            elif nested:
                base = Path("produces", "exe", "with-external", "nested")
                srcs = [
                    Path(base, ".codeblocks"),
                    Path(base, "src"),
                    Path(base, "CMakeLists.txt")
                ]
        elif wo_external:
            if flat:
                base = Path("produces", "exe", "wo-external", "flat")
                srcs = [
                    Path(base, "EMPTY")
                ]
            elif nested:
                base = Path("produces", "exe", "wo-external", "nested")
                srcs = [
                    Path(base, "EMPTY")
                ]
    elif lib:
        if with_external:
            if flat:
                base = Path("produces", "lib", "with-external", "flat")
                srcs = [
                    Path(base, ".codeblocks"),
                    Path(base, "include"),
                    Path(base, "src"),
                    Path(base, "CMakeLists.txt")
                ]
            elif nested:
                base = Path("produces", "lib", "with-external", "nested")
                srcs = [
                    Path(base, "EMPTY")
                ]
        elif wo_external:
            if flat:
                base = Path("produces", "lib", "wo-external", "flat")
                srcs = [
                    Path(base, "EMPTY")
                ]
            elif nested:
                base = Path("produces", "lib", "wo-external", "nested")
                srcs = [
                    Path(base, "EMPTY")
                ]

    tgt = Path(".")
    for src in srcs:
        shutil.move(src, tgt)
    shutil.rmtree(Path("produces"))


if __name__ == "__main__":
    main()
