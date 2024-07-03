# objective: this is utility function file where we have functions used in automation scripts in each study folder
# created date : 06 March 2024
# reviewed : Reviewed by VAB
# created by : PYB
import os
import shutil
import sys
import platform


# this method is for deleting the files from study folder to execute the study in admore solver
# check for eprf, log and CACHE folder and delete if they exists in study folder
# Passing directory location as parameter to this function
def remove_study_files(study_folder_path):
    status1 = 0
    try:
        for root, folder, file in os.walk(study_folder_path):
            if "CACHE" in root:
                print("Deleting the CACHE folder", root)
                print("-------------------------------------------------------------------------------------------")
                shutil.rmtree(root)
            for i in file:
                if i.endswith(".log") or i.endswith(".eprf") or i.endswith(".Elog") or i.endswith(
                        "MOR.STOP.SIGNAL") or i.endswith("WLM.STOP.SIGNAL"):
                    print("Deleting the file", i)
                    os.remove(os.path.join(root, i))
        print("No more Folders or files to delete")
        print("-------------------------------------------------------------------------------------------")
        status1 = 1
        return status1
    except:
        print("No files found to delete")
        print("-------------------------------------------------------------------------------------------")
        status1 = 0
        return status1


# this method is for fetch the path of EPRF and study.log file inside the study folder location
# these paths will be fed to next function to existence of these files in study folder
# Passing directory location as parameter to this function
def get_eprf_log_filepaths(dir_path):
    s_filePath = dir_path.strip('\n')
    s_baseFolder = os.path.split(dir_path)
    s_basename = (s_baseFolder[-1])
    sourceLog = (s_baseFolder[-1] + ".log")
    sourceLogPath = os.path.join(dir_path, sourceLog)
    sourceEPRF = (s_baseFolder[-1] + ".eprf")
    sourceEPRFPath = os.path.join(dir_path, sourceEPRF)
    return sourceLogPath, sourceEPRFPath, s_filePath, s_basename


# this method is to check the existence of EPRF file inside the study folder location and
# its size should be more than 0 KB
# Passing EPRF file location as parameter to this function
def check_eprf_exists(file_path):
    status2 = 0
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        print(f"The file '{file_path}' exists and has a non-zero size.")
        status2 = 1
    else:
        print(f"The file '{file_path}' either does not exist or has a zero size.")
        status2 = 0
    return status2


# this method is to check the existence of Study.log file inside the study folder location and
# its size should be more than 0 KB
# Passing Log file location as parameter to this function
def check_log_exists(log_path):
    if os.path.exists(log_path) and os.path.getsize(log_path) > 0:
        print("*******************")
        print(log_path)
        print(f"The file '{log_path}' exists and has a non-zero size.")
        f = open(log_path, 'r')
        lines = f.readlines()
        status3 = 0
        for each_line in reversed(lines):
            if "NORMAL TERMINATION,EXIT MESSAGE" in each_line:
                status3 = 1
                break
        f.close()

    else:
        print(f"The file '{log_path}' either does not exist or has a zero size.")
        status3 = 0
    return status3


# this method is to check the existence of VE and MOR files inside the study folder location and
# MOR file is used for execution of ADMORE solver
# VE file is used for session run in VIEWER in VE
# Passing VE and MOR files location as parameter to this function
def get_mor_ve_scriptpath(dir_path):
    s_filePath = dir_path.strip('\n')
    s_baseFolder = os.path.split(dir_path)
    s_basename = (s_baseFolder[-1])
    MORScript = (s_baseFolder[-1] + "_MOR.py")
    MORScriptPath = os.path.join(dir_path, MORScript)
    VEScript = (s_baseFolder[-1] + "_VE.py")
    VEScriptPath = os.path.join(dir_path, VEScript)
    return MORScriptPath, VEScriptPath, s_basename, s_filePath
