# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import dis
import marshal
import sys

def parse_file(filename):
    if filename.endswith(".pyc"):
        parse_pyc_file(filename)
    elif filename.endswith(".py"):
        parse_py_file(filename)
    else:
        raise Exception("must end with .pyc or .py")

def parse_py_file(filename):
    with open(filename, "r") as f:
        source = f.read()
        co = compile(source, filename, "exec")
    parse_co(co)

def parse_pyc_file(filename):
    header_size = 12 if sys.version_info > (3, 3) else 8
    with open(filename, "r") as f:
        f.read(header_size)
        co = marshal.load(f)
    parse_co(co)

def parse_co(co):
    import dis
    dis.dis(co)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    parse_py_file(filename)
