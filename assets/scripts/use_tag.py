import sys
import re

__file = None
__lines = []

__img_height = '30px'
__img_src = 'assets/tags/'

__tag_pattern = '/.+//'

def __read_file (name):
    try:
        global __file
        __file = open (name, 'r')
    except:
        print ('Error: Cannot read file.')
        sys.exit (1)

def __process_args ():
    if len (sys.argv) <= 1:
        print ('Error: No argument supplied.')
        sys.exit (1)
    __read_file (sys.argv [1])

def __read_lines ():
    global __file
    global __lines
    for line in __file:
        __lines.append (line.strip ())

def __substitute_tags ():
    global __img_height
    global __img_src
    global __lines
    global __tag_pattern
    img_open = '<img height="' + __img_height + '" src="' + __img_src;
    img_close = '" />';
    tag_pattern = re.compile (__tag_pattern)
    for line in __lines:
        targets = tag_pattern.findall (line)
        targets = [s[1:-2] for s in targets]
        print (targets)

def run ():
    __process_args ()
    __read_lines ()
    __substitute_tags ()

run ()
