import os


def main():

    rm_external = "{% if cookiecutter._keep_external_directory -%} false {%- else -%} true {%- endif %}",
    rm_include = "{% if cookiecutter.keep_include_directory -%} false {%- else -%} true {%- endif %}",

    paths = []
    if rm_external:
        base = "My project doesn't have external dependencies"
        paths.append(os.path.join(base, "adding", "src", "adding.c"))
        paths.append(os.path.join(base, "adding", "src"))
        paths.append(os.path.join(base, "adding", "include", "adding.h"))
        paths.append(os.path.join(base, "adding", "include"))
        paths.append(os.path.join(base, "adding", "CMakeLists.txt"))
        paths.append(os.path.join(base, "adding"))
        paths.append(base)

    if rm_include:
        base = "include"
        paths.append(os.path.join(base, "lib1", "header1.h"))
        paths.append(os.path.join(base, "lib1"))
        paths.append(os.path.join(base))


    for path in paths:
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else os.rmdir(path)

if __name__ == "__main__":
    main()
