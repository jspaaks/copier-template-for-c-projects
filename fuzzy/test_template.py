import pytest
import subprocess
import yaml
import itertools
from pathlib import Path
import random


def make_parameterization(keys, values):
    d = {key: value for (key, value) in zip(keys, values)}
    ident = ",".join(["{}={}".format(key, value) for (key, value) in zip(keys, values)])
    marks = [
        pytest.mark.skip("producesexe and produceslib are both False") if d["producesexe"] == False and d["produceslib"] == False else None,
    ]
    return pytest.param(d, id=ident, marks=[mark for mark in marks if mark is not None])


def get_params():
    with open("copier.yml", "r") as fid:
        copier_config = yaml.safe_load(fid)
    boolset = {True, False}
    data = {
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
    valuess_shuffled = valuess
    return [make_parameterization(data.keys(), values) for values in valuess_shuffled]


@pytest.fixture(scope="module", params=get_params())
def generated(tmp_path_factory, request):
    defaults = {
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
    subprocess.run(["copier", "copy", "--data-file", data_file, ".", outputdir ])
    return {
        "answers": answers,
        "directory": outputdir
    }


def test_assets_generation(generated):
    add_assets = generated["answers"]["add_assets"]
    base = generated["directory"] / generated["answers"]["projectname"]
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
    for d in directories:
        assert add_assets == d.is_dir()
    for f in files:
        assert add_assets == f.is_file()


def test_clang_format_generation(generated):
    add_clang_format = generated["answers"]["add_clang_format"]
    base = generated["directory"] / generated["answers"]["projectname"]
    files = [
        base / ".clang-format"
    ]
    for f in files:
        assert add_clang_format == f.is_file()


def test_codeblocks_generation(generated):
    add_codeblocks = generated["answers"]["add_codeblocks"]
    base = generated["directory"] / generated["answers"]["projectname"]
    directories = [
        base / generated["answers"]["build_directory"] / "codeblocks"
    ]
    files = [
        base / ".codeblocks" / "project.cbp",
        base / ".codeblocks" / "project.layout"
    ]
    for d in directories:
        assert add_codeblocks == d.is_dir()
    for f in files:
        assert add_codeblocks == f.is_file()
