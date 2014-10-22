bravo
=====

A tool to work with html element classes - for porting between/refactoring design frameworks.

Bravo is your friend if you want to transform something like
`<div class="g one-whole">` to `<div class="small-12 columns">`

Bravo is more flexible than that, and allows you to perform
quick search and replace only on "class" attributes inside any
html files - including Django templates, with inline logic.

This tool was created to assist designers at Instamojo port the
codebase from using inuit.css to Zurb Foundation - it needed
much experimentation and we wanted to have a method to make the
changes where the rules for each transformation are documented.

usage
-----

Assuming you have the folder layout:
  - project
    - design
      - templates
        - *.html

Follow these steps:
 - `$ cd project/design`
 - `$ bravo --create-config`
 - Edit `bravo.json` file just created in the working directory.


editing config file
-------------------

Your config file might look something like this::

    [
        {"search": "g", "replace": "columns", "skip": ""},
        {"search": "one-full", "replace": "small-12", "skip": ""},
        {"search": "one-half", "replace": "small-6", "skip": ""}
    ]

Each of the search,replace,skip patterns performs a single search
and replace task. You can chain as many as you need.

search
^^^^^^
Specify one or more class-names, bravo will consider a match if
ALL of the classes mentioned here are found.

replace
^^^^^^^
One or more classes that should replace the classes searched for.
If number_of(search) is same as number_of(replace) classes, bravo
will replace them one-for-one in the order they appear. Else it
will attempt to replace and remove or append other classes at
the end.

skip
^^^^
You can specify one or more class-names here. If all the classes
specified here are found, we skip the search-replace task and
move on.


installation
------------

Clone this repository somewhere, is you are using virtualenv,
create one using `mkvirtualenv bravo`.

Now run `python setup.py install`

You should be able to invoke `bravo` from your command line.

If you encounter a permission error (if you are not using virtualenv)
then you may want to add `sudo` before the setup command.


