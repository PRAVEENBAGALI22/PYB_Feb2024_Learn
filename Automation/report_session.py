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
from FetchPathsUtility import *

file_path = constants_paths.report_file_path
file_ptr = open(file_path, 'r')
lines = file_ptr.readlines()

for line in lines:
    passed_count = line.split().count("PASSED")
    if passed_count == 2:
        study_dir = line.split()[0]
        sourceEPRFPath = get_eprf_log_filepaths(study_dir)
        passed_eprf_file= sourceEPRFPath[1]
        final_eprf_file_passed = r"C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\scipts\eprf_passed_filelst.txt"
        file_ptr1 = open(final_eprf_file_passed,'a')
        file_ptr1.write(passed_eprf_file)
        file_ptr1.write('\n')
        final_log_file_passed = r"C:\G\Temp\MORUnitTests\ADMORE_TESTBATTERY_MASTER\scipts\log_info_passed.txt"
        file_ptr2 = open(final_log_file_passed, 'a')
        passed_log_file = sourceEPRFPath[0]
        study_log_file = open(passed_log_file, 'r')
        log_line_lst = study_log_file.readlines()
        log_last20line_lst = log_line_lst[-20:]
        file_ptr2.write(passed_eprf_file)
        file_ptr2.write('\n')
        for l in log_last20line_lst:
            file_ptr2.write(l)
        file_ptr2.write('\n')
        file_ptr2.write("####################################################################################################################################################################")
        file_ptr2.write('\n')
        file_ptr2.write('\n')
