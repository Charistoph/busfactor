# -*- coding: utf-8 -*-

"""Console script for dao."""

import click

from busfactor.cli.ls import ls
from busfactor.cli.mv import mv
from busfactor.cli.head import head
from busfactor.cli.cat import cat
from busfactor.utils import setup_logging


@click.group()
@click.option('-v', '--verbose', is_flag=True, default=False, help='Turn on debug logging')
@click.pass_context
def cli(context, verbose):
    """busfactor's CLI. With it, you can perform pretty much all operations you desire
        Shown below are all the possible commands you can use.

        Run ::

            $ busfactor --help

        To get an overview of the possibilities.
    """
    setup_logging(verbose)


cli.add_command(ls)
cli.add_command(mv)
cli.add_command(head)
cli.add_command(cat)
