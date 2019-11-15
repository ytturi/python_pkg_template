#Commands File
# * Listener - start listening for app registration
from logging import getLogger
import click

from python_pkg_template.confs import read_configs, init_logger


@click.command()
@click.option('-i', '--init', type=str, help='Initialize a demo Config File to use')
@click.option('-c', '--config-file', type=str, help='Config File to use')
@click.option('-v', '--verbose', type=str, help='Add verbosity to log (log-level INFO)')
@click.option('-d', '--debug', type=str, help='Set logger to DEBUG')
def do_smth(init, config_file, verbose, debug):
    if init:
        init_configs(config_file)
    read_configs(config_file)
    init_logger(verbose, debug)
    logger = getLogger('INIT')
    logger.info('INITIALIZED')

if __name__ == '__main__':
    do_smth()
