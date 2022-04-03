import contextlib
import io
import sys
import unittest
import re


def parse_katas_score(classes, result):
    katas = 0
    for name, cls in classes:
        regex = r"FAIL: .*" + name
        match = re.search(regex, result)
        if not match:
            katas += int(cls.__doc__.split('Kata')[0].strip())
    print('---------------------------------------')
    print(f'Total Python Katas: {katas}')
    print('---------------------------------------')


@contextlib.contextmanager
def err_to(file):
    old_err = sys.stderr
    sys.stderr = file
    yield
    sys.stderr = old_err


def unittest_runner(classes):
    result = io.StringIO()
    with err_to(result):
        unittest.main(exit=False)
    result.seek(0)
    result = str(result.read())
    parse_katas_score(
        classes,
        result
    )
    print(result)
