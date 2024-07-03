# Objective: Aim of the scrpit is to run the ADMORE and VE execution one after another based on STATUS in report file
# First of all ADMORE solver executed with _MOR.py and when status in reprt file "PASSED, we execute
# Secondly VE is executed and status is updated accordlingy

import os
import shutil
import sys
import platform
import time

# fetching the current directory from this API
dir_path = os.path.dirname(os.path.realpath(__file__))
# constructing the path where all constants and master files are present
custom_script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(dir_path)))),
                                  "ADMORE_TESTBATTERY_MASTER")
sys.path.append(custom_script_path)
# import the paths defined in the constants_path file
import constants_paths
# import the functions defined in the FetchPathsUtility file
from FetchPathsUtility import *

MORScriptPath, VEScriptPath, s_basename, s_filePath = get_mor_ve_scriptpath(dir_path)
pyPath = constants_paths.python_path

file_path = constants_paths.report_file_path
file_ptr = open(file_path, 'a')

status_words = ["PASSED", "FAILED"]
status = status_words[0]

# with this function we get _MOR.py file present in the study folder
# when this file is found we execute the file in python
# when the STATUS is "PASSED" we proceed for _VE.py file execution
if os.path.exists(MORScriptPath):
    print("----------------ADMORE Solver is executing--------------------")
    cmd = '%s %s' % (pyPath, MORScriptPath)
    os.system(cmd)
    print("----------------End of ADMORE Solver execution----------------")
    for line in reversed(open(file_path).readlines()):
        string_to_check = s_filePath
        if string_to_check in line:
            status = line.split('\t')[-1]
            break
else:
    print("MORScriptPath doesn't exists")

if status_words[0] in status:
    # ------------------------------------------------------------------------------------------------#
    VEPath = constants_paths.viewer_path
    #context = r"-activeconfig Trade:cis VisualViewer -sessionrun"
    context = r" -activeconfig Others:VIEWER -activeapp VisualViewerGeneral -sessionrun"
    exit_cmd = r"-exit"
    scriptname = VEScriptPath

    print("Visual Environment Version Launching")
    print("-------------------------------------------------------------------------------------------")
    cmd = '%s %s %s %s' % (VEPath, context, scriptname, exit_cmd)
    print(cmd)
    os.system(cmd)
    print("-------------------------------------------------------------------------------------------")

elif status_words[1] in status:
    write_status = '\t' + status_words[1]
    file_ptr.write(write_status)
    file_ptr.write('\n')

file_ptr.close()
