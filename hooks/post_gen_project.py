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
                pass
            elif nested:
                pass
        elif wo_external:
            if flat:
                pass
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
                pass
        elif wo_external:
            if flat:
                pass
            elif nested:
                pass
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
                pass
        elif wo_external:
            if flat:
                pass
            elif nested:
                pass

    tgt = Path(".")
    for src in srcs:
        shutil.move(src, tgt)
    shutil.rmtree(Path("produces"))


if __name__ == "__main__":
    main()
