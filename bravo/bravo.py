"""Bravo is a tool that works with HTML styles."""

import click
from filewalker import file_walker
@click.option('--sample', default=0, help='Process these many files and stop.')
@click.argument('pattern', default='*.*')
@click.argument('target_directory', default='.')
@click.command()
def run(target_directory, pattern, sample):
    for i,filepath in enumerate(file_walker(target_directory, pattern)):
        if sample > 0 and i == sample:
            break

        print i, filepath


if __name__ == '__main__':
    run()
