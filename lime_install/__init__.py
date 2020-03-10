__version__ = '0.1.0'


import click
import venv

import pathlib


def create_venv():
    path = pathlib.Path().joinpath(pathlib.Path().absolute(), '/lime' )
    venv.create(pathlib.Path().absolute())
