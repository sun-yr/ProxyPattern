# -*- coding:utf-8 -*-
__author__ = 'Delbert'

import json
import argparse
import os


def parse_args():
    """
    :rtype : str
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help='File to progress.', default='patterns.json')
    parser.add_argument("-o", help='File after process to save.')
    args = parser.parse_args()
    file_path = ''
    file_input = ''

    if args.i:
        # Get the name of the file to parse.
        file_input = args.i.split(os.sep)[-1]

        # Get the path to save file output.
        sep_path = args.i.split(os.sep)
        if sep_path[0:-1]:
            file_path = os.sep.join(sep_path[0:-1])
        else:
            file_path = os.getcwd()
    else:
        # If there is no file input.
        print("Error: No input file.")
        exit(-1)

    if args.o:
        file_output = args.o
    else:
        file_output = file_input + ".output.txt"

    return file_path, file_input, file_output


def get_path(file_path, file_input, file_output):
    full_in_path = file_path + os.sep + file_input
    full_out_path = file_path + os.sep + file_output
    # Some words to console.
    print("The file input is {0}".format(full_in_path))
    print("The file output is {0}".format(full_out_path))
    return full_in_path, full_out_path


def parse_json(full_inpath, full_outpath, file_path):
    # Parse json file to urls
    out = open(full_outpath, 'wt')
    json_file = open(full_inpath, 'rt')
    json_data = json.loads(json_file.read())

    for content in json_data['patterns']:
        out.write(content['pattern'] + '\n')
        print(content['pattern'])
    json_file.close()
    out.close()

    # Parse json file and convert to switchysharp.txt
    switchy_pre = '''; Summary: Rule List Converted from FoxyProxy
; Author: Delbert (i@delbert.me)
; Date: 2014-12-06
; URL: https://github.com/cnDelbert/ProxyPattern/blob/master/SwitchySharp/switchyrules.txt

#BEGIN

[Wildcard]
'''
    switchy_after = '''
[RegExp]

#END'''
    switchy_txt = open(file_path + os.sep + 'switchyrules.txt', 'wt')
    json_file = open(full_inpath, 'rt')
    json_data = json.loads(json_file.read())
    switchy_txt.write(switchy_pre)

    for content in json_data['patterns']:
        switchy_txt.write(content['pattern'] + '\n')

    json_file.close()
    switchy_txt.write(switchy_after)
    switchy_txt.close()


if __name__ == '__main__':
    file_p, file_i, file_o = parse_args()
    fi_path, fo_path = get_path(file_p, file_i, file_o)
    parse_json(fi_path, fo_path, file_p)