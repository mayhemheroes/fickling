#!/usr/local/bin/python3
from random import random
from textwrap import indent
import atheris
import sys
import io
import os
import random

with atheris.instrument_imports():
    import ast
    from fickling.pickle import Pickled

@atheris.instrument_func
def TestOneInput(data):
    try:
        Pickled.load(data)
    except ValueError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()