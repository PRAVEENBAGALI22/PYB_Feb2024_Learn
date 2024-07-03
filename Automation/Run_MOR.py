# Obejctive : Aim of this script is to generate EPRF file generated in ADMORE solver
# Before solver execution delete all files, start fresh execution
# After successful solver execution, check for EPRF and Study.log files existance and also size of these file to more than 0

import os
import shutil
import sys
import platform

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

# -----------Now executing the ADMORE Solver Unit Testing----------------#
# with this function we remove all the files present in the study folder
status1 = remove_study_files(dir_path)

admoreSolverPath = constants_paths.admoreSolverPath
casename = dir_path

# ADMORE solver execution is done in command mode with python path
print("----------------ADMORE Solver is executing--------------------")
cmd = '%s %s' % (admoreSolverPath, casename)
print(cmd)
os.system(cmd)
print("----------------End of ADMORE Solver execution----------------")

# with this function we get eprf and log files present in the study folder
get_eprf_log_filepaths(dir_path)
sourceLogPath, sourceEPRFPath, s_filePath, s_basename, = get_eprf_log_filepaths(dir_path)
print('sourceLogPath, sourceEPRFPath', sourceLogPath, sourceEPRFPath, s_filePath, s_basename)

# with this function we get eprf file present and size is more than 0 KB in the study folder
status2 = check_eprf_exists(sourceEPRFPath)

# with this function we get log file present and size is more than 0 KB in the study folder
status3 = check_log_exists(sourceLogPath)

# open the report file and write the status of AMDORE solver execution to file
file_path = constants_paths.report_file_path
file_ptr = open(file_path, 'a')
if file_ptr == None:
    print("File path doesn't exists\n")
    sys.exit()

status_words = ["PASSED", "FAILED"]

if status2 == 1 and status3 == 1:
    file_ptr.write(s_filePath + '\t' + status_words[0])
    print(s_filePath + "_MOR" + '\t' + status_words[0])
else:
    file_ptr.write(s_filePath + '\t' + status_words[1])
    print(s_filePath + "_MOR" + '\t' + status_words[1])
file_ptr.close()
