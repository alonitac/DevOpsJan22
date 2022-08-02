import json
import os
import os
import glob

# import tarfile
import ntpath
import fileinput
# from datetime import datetime
#
# dt_string = datetime.now().strftime("%d-%m-%Y")
# head, tail = ntpath.split(dir_path)
# f_name = 'backup_' + tail + '_' + dt_string
# tar = tarfile.open(f_name + ".tar.gz", "w:gz")
# tar.add(dir_path, arcname=f_name)
# tar.close()

# def replace_in_file(file_path, text, replace_text):
#     head, tail = ntpath.split(file_path)
#     with fileinput.FileInput(tail, inplace=True) as file:
#         for line in file:
#             print(line.replace(text, replace_text), end='')
#     replace_in_file(dir_path, 'text', 'replace_text')



def json_configs_merge(*json_paths):

if __name__ == '__main__':

    # path1 = 'local.json'
    # path2 = 'default.json'
    path1 = '/home/go/Pycharm/Boot_Camp/python_katas/kata_2/local.json'
    path2 = '/home/go/Pycharm/Boot_Camp/python_katas/kata_2/default.json'
    files = (path1, path2)
    json_configs_merge(path1)
