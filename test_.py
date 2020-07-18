# coding: utf-8
from os.path import dirname, join

import pytest

import _ as task

samples = [
    # SAMPLES
]

random = [

]

files = [

]

timeout_sec = 2


@pytest.mark.timeout(timeout_sec)
@pytest.mark.parametrize('i,o', samples+random)
def test_samples(i, o, capsys):
    _test(i, o, capsys)


@pytest.mark.timeout(timeout_sec)
@pytest.mark.parametrize('fi,fo', files)
def test_files(fi, fo, capsys):
    _test(
        open(join(dirname(__file__), fi), 'r').read().splitlines(),
        open(join(dirname(__file__), fo), 'r').read().strip(),
        capsys
    )


def _test(i, o, capsys):
    assert task.solve(*i) == o
    out, _ = capsys.readouterr()
    if out:
        print(out)
        assert False, 'Remove print commands'
