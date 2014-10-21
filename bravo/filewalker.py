import os
import fnmatch

def file_walker(base_directory, file_pattern):
    """generator, lists all files matching pattern inside base_directory, searches recursively"""
    for path, dirs, files in os.walk(os.path.abspath(base_directory)):
        for filename in fnmatch.filter(files, file_pattern):
            filepath = os.path.join(path, filename)
            yield filepath

