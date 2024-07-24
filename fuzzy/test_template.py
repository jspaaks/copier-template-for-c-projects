import pytest
import subprocess
import yaml
from pathlib import Path
import itertools
import random
import os


def get_parameterization(keys, values):
    d = {key: value for (key, value) in zip(keys, values)}
    ident = ",".join(["{}={}".format(key, value) for (key, value) in zip(keys, values)])
    marks = [
        pytest.mark.skip("producesexe and produceslib are both False") if d["producesexe"] == False and d["produceslib"] == False else None
    ]
    return pytest.param(d, id=ident, marks=[mark for mark in marks if mark is not None])


def get_parameterizations():
    with open("copier.yml", "r") as fid:
        copier_config = yaml.safe_load(fid)
    boolset = {True, False}
    data = {
        "add_answers": boolset,
        "add_assets": boolset,
        "add_clang_format": boolset,
        "add_cmake": boolset,
        "add_codeblocks": boolset,
        "add_external": boolset,
        "add_test": boolset,
        "build_directory": list(copier_config["build_directory"]["choices"].keys())[:2],
        "exename": ["calculator", "navigator"],
        "external_directory": list(copier_config["external_directory"]["choices"].keys())[:2],
        "libname": ["operations", "directions"],
        "libpurpose": copier_config["libpurpose"]["choices"].values(),
        "nested": boolset,
        "producesexe": boolset,
        "produceslib": boolset,
        "projectname": ["calculator-project", "navigator-project"]
    }
    valuess = itertools.product(*data.values())
    tmp = os.environ.get("NFUZZY", None)
    nfuzzy = None if tmp is None else int(tmp)
    assert nfuzzy is not None, "These tests need NFUZZY environment variable"
    valuess_sampled = random.sample(list(valuess), nfuzzy)
    return [get_parameterization(data.keys(), values) for values in valuess_sampled]


@pytest.fixture(scope="module", params=get_parameterizations())
def generated(tmp_path_factory, request):
    """
    This fixture's parameterization depends on the environment
    variable NFUZZY being present and containing a (string that
    can be parsed into a) valid integer.
    """

    defaults = {
        "add_answers": False,
        "add_assets": True,
        "add_clang_format": True,
        "add_cmake": True,
        "add_codeblocks": True,
        "add_external": True,
        "add_test": True,
        "build_directory": "build",
        "exename": "calculator",
        "external_directory": "external",
        "libname": "operations",
        "libpurpose": "both",
        "nested": True,
        "producesexe": True,
        "produceslib": True,
        "projectname": "calculator-project"
    }
    answers = defaults
    answers.update(request.param)

    basedir = tmp_path_factory.mktemp("base")
    inputdir = basedir / "input"
    inputdir.mkdir()
    outputdir = basedir / "output"
    outputdir.mkdir()

    data_file = inputdir / "data.yml"
    with open(data_file, "wt") as fid:
        yaml.dump(answers, fid)
    subprocess.run(f"copier copy --data-file { str(data_file) } --vcs-ref=HEAD template { str(outputdir) }", shell=True, check=True)
    return {
        "answers": answers,
        "directory": outputdir
    }


def meets_expected_presence(*, ispresent=True, directories=None, files=None):
    if directories is not None:
        for d in directories:
            assert True if d is None else ispresent == d.is_dir(), f"Directory '{ d }' was unexpectedly { "not present" if ispresent else "present" }."
    if files is not None:
        for f in files:
            assert True if f is None else ispresent == f.is_file(), f"File '{ f }' was unexpectedly { "not present" if ispresent else "present" }."
    return True

def get_answers(answers, *keys):
    return [ answers[key] for key in keys ]


def test_assets_generation(generated):
    add_assets, projectname = \
            get_answers(generated["answers"], "add_assets", "projectname")
    base = generated["directory"] / projectname
    directories = [
        base / "assets",
        base / "assets" / "fonts",
        base / "assets" / "images",
        base / "assets" / "sounds"
    ]
    files = [
        base / "assets" / "fonts" / "font.ttf",
        base / "assets" / "images" / "image.bmp",
        base / "assets" / "sounds" / "sound.wav"
    ]
    assert meets_expected_presence(ispresent=add_assets, directories=directories, files=files)


def test_clang_format_generation(generated):
    add_clang_format, projectname = \
            get_answers(generated["answers"], "add_clang_format", "projectname")
    base = generated["directory"] / projectname
    files = [
        base / ".clang-format"
    ]
    assert meets_expected_presence(ispresent=add_clang_format, files=files)

def test_cmake_generation(generated):
    add_assets, add_cmake, add_external, add_test, build_directory, exename, external_directory, libname, nested, producesexe, produceslib, projectname = \
            get_answers(generated["answers"], "add_assets", "add_cmake", "add_external", "add_test", "build_directory", "exename", "external_directory", "libname", "nested", "producesexe", "produceslib", "projectname")
    base = generated["directory"] / projectname
    directories = [ base / build_directory / "cmake" ]
    files = [ base / "CMakeLists.txt" ]
    if producesexe:
        if nested:
            files += [ base / "src" / exename / "CMakeLists.txt"]
        else:
            files += [ base / "src" / "CMakeLists.txt" ]
    if produceslib:
        if nested:
            files += [ base / "src" / libname / "CMakeLists.txt" ]
            if add_test:
                files += [ base / "test" / libname / "CMakeLists.txt" ]
        else:
            files += [ base / "src" / "CMakeLists.txt" ]
            if add_test:
                files += [ base / "test" / "CMakeLists.txt" ]
    if add_assets:
        files += [
            base / "assets" / "CMakeLists.txt",
            base / "assets" / "fonts" / "CMakeLists.txt",
            base / "assets" / "images" / "CMakeLists.txt",
            base / "assets" / "sounds" / "CMakeLists.txt"
        ]
    if add_external:
        files += [
            base / external_directory / "CMakeLists.txt",
        ]
    assert meets_expected_presence(ispresent=add_cmake, directories=directories, files=files)


def test_codeblocks_generation(generated):
    add_codeblocks, projectname, build_directory = \
            get_answers(generated["answers"], "add_codeblocks", "projectname", "build_directory")
    base = generated["directory"] / projectname
    directories = [
        base / build_directory / "codeblocks"
    ]
    files = [
        base / ".codeblocks" / "project.cbp",
        base / ".codeblocks" / "project.layout"
    ]
    assert meets_expected_presence(ispresent=add_codeblocks, directories=directories, files=files)
