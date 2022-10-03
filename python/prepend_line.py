import os
from fnmatch import fnmatch

def list_files(root, pattern):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                file_name = os.path.join(path, name)
                print(file_name)

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

def prepend_multiple_lines(file_name, list_of_lines):
    """Insert given list of strings as a new lines at the beginning of a file"""
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open given original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Iterate over the given list of strings and write them to dummy file as lines
        for line in list_of_lines:
            write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

def main():
    root = 'C:\\Users\\adrien\\Documents\\MMS\\WS\\telemedaq_mobile\\src\\components'
    pattern = '*.js'
    line1 = "/* eslint-disable @typescript-eslint/explicit-module-boundary-types */"
    line2 = "/* eslint-disable no-undef */"

    list_files(root, pattern)
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                file_name = os.path.join(path, name)
                print('*** Insert a line at the top of a file ***')
                # Insert a line before the first line of a file 'sample.txt'
                # prepend_line(file_name, line1)
                print('*** Insert multiple lines at the beginning of a file ***')
                list_of_lines = [line1, line2]
                # Insert strings in a list as new lines at the top of file 'sample.txt'
                prepend_multiple_lines(file_name, list_of_lines)
if __name__ == '__main__':
   main()
