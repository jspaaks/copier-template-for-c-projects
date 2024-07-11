import os
from pathlib import Path
import shutil


def main():

    produces = "{{ cookiecutter.produces }}"
    rm_external = "{{ cookiecutter.external_directory }}" == "My project doesn't have external dependencies"
    rm_assets = "{{ cookiecutter.keep_assets }}" == "False"

    paths = []

    if rm_assets:
        paths.append(Path("assets", "fonts", "font.ttf"))
        paths.append(Path("assets", "fonts", "CMakeLists.txt"))
        paths.append(Path("assets", "fonts", "README.md"))
        paths.append(Path("assets", "fonts"))
        paths.append(Path("assets", "sounds", "sound.wav"))
        paths.append(Path("assets", "sounds", "CMakeLists.txt"))
        paths.append(Path("assets", "sounds", "README.md"))
        paths.append(Path("assets", "sounds"))
        paths.append(Path("assets", "images", "CMakeLists.txt"))
        paths.append(Path("assets", "images", "image.bmp"))
        paths.append(Path("assets", "images", "README.md"))
        paths.append(Path("assets", "images"))
        paths.append(Path("assets", "CMakeLists.txt"))
        paths.append(Path("assets"))

    if rm_external:
        base = "My project doesn't have external dependencies"
        paths.append(Path(base, "addition", "src", "addition.c"))
        paths.append(Path(base, "addition", "src"))
        paths.append(Path(base, "addition", "include", "addition.h"))
        paths.append(Path(base, "addition", "include"))
        paths.append(Path(base, "addition", "CMakeLists.txt"))
        paths.append(Path(base, "addition"))
        paths.append(Path(base, "subtraction", "src", "subtraction.c"))
        paths.append(Path(base, "subtraction", "src"))
        paths.append(Path(base, "subtraction", "include", "subtraction.h"))
        paths.append(Path(base, "subtraction", "include"))
        paths.append(Path(base, "subtraction", "CMakeLists.txt"))
        paths.append(Path(base, "subtraction"))
        paths.append(Path(base, "CMakeLists.txt"))
        paths.append(base)

    filesets = {
        "both": [
            Path("produces", "both", ".codeblocks", "project.cbp"),
            Path("produces", "both", ".codeblocks"),
            Path("produces", "both", "include", "CMakeLists.txt"),
            Path("produces", "both", "include", "libcalculator", "ops.h"),
            Path("produces", "both", "include", "libcalculator"),
            Path("produces", "both", "include"),
            Path("produces", "both", "src", "calculator", "main.c"),
            Path("produces", "both", "src", "calculator", "CMakeLists.txt"),
            Path("produces", "both", "src", "calculator"),
            Path("produces", "both", "src", "libcalculator", "multiplication.h"),
            Path("produces", "both", "src", "libcalculator", "multiplication.c"),
            Path("produces", "both", "src", "libcalculator", "division.h"),
            Path("produces", "both", "src", "libcalculator", "division.c"),
            Path("produces", "both", "src", "libcalculator", "CMakeLists.txt"),
            Path("produces", "both", "src", "libcalculator"),
            Path("produces", "both", "src", "CMakeLists.txt"),
            Path("produces", "both", "src"),
            Path("produces", "both", "CMakeLists.txt"),
            Path("produces", "both")
        ],
        "exe": [
            Path("produces", "exe", ".codeblocks", "project.cbp"),
            Path("produces", "exe", ".codeblocks"),
            Path("produces", "exe", "src", "multiplication.h"),
            Path("produces", "exe", "src", "multiplication.c"),
            Path("produces", "exe", "src", "main.c"),
            Path("produces", "exe", "src", "division.h"),
            Path("produces", "exe", "src", "division.c"),
            Path("produces", "exe", "src"),
            Path("produces", "exe", "CMakeLists.txt"),
            Path("produces", "exe")
        ],
        "lib": [
            Path("produces", "lib", ".codeblocks", "project.cbp"),
            Path("produces", "lib", ".codeblocks"),
            Path("produces", "lib", "include", "multiplication.h"),
            Path("produces", "lib", "include", "division.h"),
            Path("produces", "lib", "include"),
            Path("produces", "lib", "src", "multiplication.c"),
            Path("produces", "lib", "src", "division.c"),
            Path("produces", "lib", "src"),
            Path("produces", "lib", "CMakeLists.txt"),
            Path("produces", "lib")
        ]
    }

    if produces == "an executable":
        for item in filesets["both"] + filesets["lib"]:
            paths.append(item)
        srcs = [
            Path("produces", "exe", ".codeblocks"),
            Path("produces", "exe", "src"),
            Path("produces", "exe", "CMakeLists.txt")
        ]
        tgt = Path(".")
        for src in srcs:
            shutil.move(src, tgt)
        paths.append(Path("produces", "exe"))
        paths.append(Path("produces"))

    elif produces == "a library":
        for item in filesets["both"] + filesets["exe"]:
            paths.append(item)
        srcs = [
            Path("produces", "lib", ".codeblocks"),
            Path("produces", "lib", "include"),
            Path("produces", "lib", "src"),
            Path("produces", "lib", "CMakeLists.txt")
        ]
        tgt = Path(".")
        for src in srcs:
            shutil.move(src, tgt)
        paths.append(Path("produces", "lib"))
        paths.append(Path("produces"))

    elif produces == "both":
        for item in filesets["exe"] + filesets["lib"]:
            paths.append(item)
        srcs = [
            Path("produces", "both", ".codeblocks"),
            Path("produces", "both", "include"),
            Path("produces", "both", "src"),
            Path("produces", "both", "CMakeLists.txt")
        ]
        tgt = Path(".")
        for src in srcs:
            shutil.move(src, tgt)

        paths.append(Path("produces", "both"))
        paths.append(Path("produces"))



    for path in paths:
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)


if __name__ == "__main__":
    main()
