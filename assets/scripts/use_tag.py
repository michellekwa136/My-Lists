import sys
import re

__file = None
__file_name = ''
__lines = []

__img_height = '20px'
__img_src = 'assets/tags/'

__tag_pattern = '/[a-z| ]+//'
__tag_open = '/'
__tag_close = '//'
__tag_file_type = 'png'

def __read_file ():
    print ('DEBUG: Reading file...')
    try:
        global __file
        global __file_name
        __file = open (__file_name, 'r')
    except:
        print ('Error: Cannot read file.')
        sys.exit (1)

def __write_file ():
    print ('DEBUG: Writing to file...')
    try:
        global __file
        global __file_name
        __file = open (__file_name, 'w')
    except:
        print ('Error: Cannot write to file.')
        sys.exit (1)
    global __lines
    for line in __lines:
        __file.write (line + '\n')
    __file.close ()

def __process_args ():
    if len (sys.argv) <= 1:
        print ('Error: No argument supplied.')
        sys.exit (1)
    global __file_name
    print ('DEBUG: Assigning file name...')
    __file_name = sys.argv [1]

def __read_lines ():
    global __file
    global __lines
    for line in __file:
        __lines.append (line.strip ())
    __file.close ()
    print ('DEBUG: Done reading lines...')

def __substitute_tags ():
    global __img_height
    global __img_src
    global __lines
    global __tag_pattern
    global __tag_open
    global __tag_close
    global __tag_file_type
    print ('DEBUG: Substituting tags...')
    img_open = '<img height="' + __img_height + '" src="' + __img_src;
    img_close = '.' + __tag_file_type + '" />';
    tag_pattern = re.compile (__tag_pattern)
    new_lines = []
    for line in __lines:
        targets = tag_pattern.findall (line)
        targets = [s[1:-2] for s in targets]
        for target in targets:
            line = line.replace (__tag_open + target + __tag_close,
                    img_open + target.replace (' ', '_') + img_close, 1)
        new_lines.append (line)
    __lines = new_lines

def run ():
    __process_args ()
    __read_file ()
    __read_lines ()
    __substitute_tags ()
    __write_file ()

run ()
