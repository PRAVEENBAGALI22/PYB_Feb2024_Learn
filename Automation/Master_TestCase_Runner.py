import os
import shutil
import sys
import platform
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
custom_script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(dir_path)))),
                                  "ADMORE_TESTBATTERY_MASTER")
sys.path.append(custom_script_path)
import constants_paths

pyPath = constants_paths.python_path
file_path = constants_paths.report_file_path
file_ptr = open(file_path, 'a')

file_path_testcases = r"C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\TestCase_List.txt"
file_ptr1 = open(file_path_testcases, 'r')
for line in file_ptr1.readlines():
    print(line)
    cmd = '%s %s' % (pyPath, line)
    os.system(cmd)
    dir_name = os.path.dirname(os.path.abspath(line))
    # print(dir_name)
    for line in reversed(open(file_path).readlines()):
        string_to_check = dir_name
        if string_to_check in line:
            dir_list = line.split('\t')
            if len(dir_list) != 3:
                time.sleep(10)
            else:
                continue
