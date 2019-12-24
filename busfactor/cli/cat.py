import logging

import click

from busfactor.utilities.cat import main
_logger = logging.getLogger('root')


@click.command()
@click.option('--path', '-p', help='Path of interest', default='.')
def cat(path: str) -> None:
    """
    Cats a file to terminal, pretty

    Parameters
    ----------
    path: str

    Returns
    -------
    Nonedd

    """
    _logger.info('Initiating work')
    main(path)

