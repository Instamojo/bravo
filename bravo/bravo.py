"""Bravo is a tool that works with HTML styles."""
import re
import click
import json
from filewalker import file_walker


settings = {'search': '', 'replace': '', 'skip': ''}


def get_class_names_compiled():
    class_names_regex = r"""(?:class=)(?:[\"])(?P<class_names>.+?)(?:[\"])"""
    class_names_compiled = re.compile(class_names_regex, re.VERBOSE)
    return class_names_compiled


def class_names_to_list(class_names):
    class_names = class_names.replace('  ', ' ')
    class_name_compiled = re.compile(r"""(?P<class_name>\b[\w\{\}%\-]+\b)""")
    return [x for x in class_name_compiled.findall(class_names)]


def search_classes_in_string(class_names):
    """
    :param class_names: example: "small-12 large-6 columns"
    :return: boolean
    """
    available_classes = set(class_names_to_list(class_names))
    search_classes = set(class_names_to_list(settings['search']))
    skip_classes = set(class_names_to_list(settings['skip']))
    if available_classes.issuperset(search_classes) and available_classes.isdisjoint(skip_classes):
        return True
    return False


def get_replacement_classes(class_names):
    return re.sub(r"""(\b){classname}(\b)(?![\w-])""".format(classname=settings['search']),
                     " {classname} ".format(classname=settings['replace']), class_names).strip().replace('  ',' ')


def replace_classes(template, match, replace_with):
    prefix = template[:match.start('class_names')]
    postfix = template[match.end('class_names'):]
    return prefix + replace_with + postfix


@click.option('--replace', default='', help='Replace found classes with these.')
@click.option('--skip', default='', help='Skip find-replace if these classes are found.')
@click.option('--config', default='', help='Use a specific configuration file.')
@click.option('--sample', default=0, help='Process these many files and stop.')
@click.argument('search_classes')
@click.argument('pattern', default='*.*')
@click.argument('target_directory', default='.')
@click.command()
def run(target_directory, pattern, sample, config, skip, replace, search_classes):
    global settings
    for i,filepath in enumerate(file_walker(target_directory, pattern)):
        if sample > 0 and i == sample:
            break
        if search_classes:
            settings['search'] = search_classes
            settings['replace'] = replace
            settings['skip'] = skip
            with open(filepath, 'r+') as template_file:
                template = template_file.read()
                replaced = False
                for match in get_class_names_compiled().finditer(template):
                    classes_found = search_classes_in_string(match.group('class_names'))
                    if classes_found:
                        if replace:
                            replace_with = get_replacement_classes(match.group('class_names'))
                            template = replace_classes(template, match, replace_with)
                            replaced = True
                        print "\t{start}:{end} \t{class_names} {replaced_with}".format(start=match.start('class_names'),
                                                                    end=match.end('class_names'),
                                                                    class_names=match.group('class_names'),
                                                                    replaced_with='=> {}'.format(replace_with))
                if replaced:
                    with open(filepath, 'w+') as template_file:
                        template_file.write(template)


        print i, filepath


if __name__ == '__main__':
    run()
