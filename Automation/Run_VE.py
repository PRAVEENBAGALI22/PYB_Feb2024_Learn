# Obejctive : Aim of this script is to load the EPRF file generated in previous step in VE application 
# Load the file and set the animation state to last state and apply contour and fetch the values at particular locations
# Store the values in dic and compare when we rerau the _VE.py file

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
import constants_paths
from FetchPathsUtility import *
# constructing the path where all constants and master files are present
# use of Utility_Functions from this file and use in contour session 
VV_AUTOMATION_PATH = os.path.join(custom_script_path, "Utility_Functions")
sys.path.append(os.path.abspath(VV_AUTOMATION_PATH))
from ContourClass import *

contour_class = PyContourClass()

#with this function we get eprf and log files present in the study folder
get_eprf_log_filepaths(dir_path)
sourceLogPath, sourceEPRFPath, s_filePath, s_basename, = get_eprf_log_filepaths(dir_path)
print('sourceLogPath, sourceEPRFPath', sourceLogPath, sourceEPRFPath, s_filePath, s_basename)

erf_file_path = sourceEPRFPath

from defaultmodules import *
import VistaDb
import Viewer

var1 = VCmd.Activate(1, r"VHostManagerPlugin.VhmInterface", r"VhmCommand")
var2 = VCmd.Activate(1, r"VSessionManager.Command", r"SessionCommand")
# __________________ VEAction BEGIN __________________
var3 = VCmd.Activate(1, r"VToolKit.VSectionCutInterface", r"VEAction")
VE.ChangeContext(r"Visual-Viewer")
ret = VE.ChangeSkin(r"General")
Viewer.SetFormat(32)
ret = Viewer.LoadFile(erf_file_path)
VE.Command(">>> animend()")
# __________________ VtkParameterSpaceExploration BEGIN __________________
var4 = VCmd.Activate(1, r"VToolKit.VToolKitInterface", r"VtkParameterSpaceExploration")
VCmd.SetIntValue(var4, r"ContinousUpdate", 1)
VCmd.SetGuStringValue(var4, r"FileName", erf_file_path)
# __________________ VtkContourDlg BEGIN __________________
var5 = VCmd.Activate(1, r"VToolKit.VToolKitInterface", r"VtkContourDlg")
VCmd.SetStringValue(var5, r"FileName", erf_file_path)
VCmd.SetStringValue(var5, r"ContourMethod", r"ByEntity")
VCmd.SetStringValue(var5, r"ContourParentName", r"NODE")
VCmd.SetStringValue(var5, r"ContourDisplayName", r"Displacement")
VCmd.SetStringValue(var5, r"Qualifier", r"Y")
VCmd.SetStringValue(var5, r"Encoding", r"Vector")
VCmd.SetIntValue(var5, r"ContourGrayFlag", 1)
VCmd.SetStringValue(var5, r"SpectrumDispMode", r"Smeared")
VCmd.SetStringValue(var1, r"ActiveGUI", r"Parametric Space Exploration")
VCmd.SetGuStringValue( var4, r"ParameterName", r"Thickness" )
VCmd.SetDoubleValue( var4, r"ParameterValue", 1.75  )
ret = VCmd.ExecuteCommand(var5, r"ApplyContour")


num_Frames = Viewer.GetNumFrames(erf_file_path)
# this stores the contour values of entities requested 
ref_info_text_dict = {}
ent_type = ""
result_name = ""
entity_ID_List = []  # specify the ID to be checked

cont_info_text_dict = {}
for ref_id in entity_ID_List:
    status, val = Viewer.GetContourValGivenEntityId(erf_file_path, ref_id, ent_type, result_name, num_Frames)
    cont_info_text_dict[ent_type] = result_name
    cont_info_text_dict[ref_id] = round(val, 3)

print(cont_info_text_dict)

status = 0
if comparedictionaries(ref_info_text_dict, cont_info_text_dict):
    status = 1
    
#open the report file and write the status of VE Session execution to file
file_path = constants_paths.report_file_path
file_ptr = open(file_path, 'a')
if file_ptr == None:
    print("File path doesn't exists\n")
    sys.exit()

status_words = ["PASSED", "FAILED"]

if status == 1:
    for line in reversed(open(file_path).readlines()):
        MOR_Status_Check = status_words[0]
        if MOR_Status_Check in line:
            write_status = '\t' + status_words[0]
            file_ptr.write(write_status)
            file_ptr.write('\n')
            break
    print(s_basename + "_VE" + '\t' + status_words[0])
else:
    for line in reversed(open(file_path).readlines()):
        write_status = '\t' + status_words[1]
        file_ptr.write(write_status)
        file_ptr.write('\n')
        break
    print(s_basename + "_VE" + '\t' + status_words[1])
file_ptr.close()

